from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import *



#to soft delete employee if related company is sift deleted
@receiver(post_save, sender=Company)
def update_employee(sender, instance, **kwargs):
    for i in Employee.objects.filter(company_id__is_deleted=True):
        i.soft_del()



#to send email to employee when new employee is added
@receiver(post_save, sender=Employee)
def send_email(sender, created, instance, **kwargs):
    if created:
        subject = f'Welcome {instance.first_name} {instance.last_name}'
        message = f'Hello {instance.first_name},\n\nYour employee ID has been successfully added.'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [instance.email]
        send_mail(subject, message, from_email, recipient_list)