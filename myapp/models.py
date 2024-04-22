from django.db import models
from django.contrib.auth.models import AbstractUser



#custome user to require login via email insted of username
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["username"]



# To only return items which are not soft deleted
class NotDel(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted = False)



# creating soft delete and restore methods
class SoftDel(models.Model):
    is_deleted = models.BooleanField(default=False)
    objects = NotDel()              # by changing objects to NotDel, soft-deleted items will not be called
    allobj = models.Manager()       # using allobj, all items which are not hard deleted will be called
    def soft_del(self):             # method to implement soft delete
        self.is_deleted = True
        self.save()
    def restore(self):              # method to restore soft deleted items
        self.is_deleted = False
        self.save()
    class meta:
        abstract = True             # this makes model not migrate



class Company(SoftDel):
    company_id = models.CharField(max_length=30, primary_key=True)
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.company_id + " (" + self.name + ")"
    


class Employee(SoftDel):
    employee_id = models.CharField(max_length=30, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    company_id = models.ForeignKey("Company", on_delete=models.CASCADE)
    dob = models.DateField(auto_now=False)
    email = models.EmailField(max_length=70, unique=True)
    profile_pic = models.ImageField(upload_to='images', default='images/image.png')
    def __str__(self):
        return self.first_name + " " + self.last_name
