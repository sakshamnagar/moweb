from django.core.management import BaseCommand
from django.core.mail import send_mail
from django.utils import timezone
from .models import Employee
from django.conf import settings


#To automate sending bday emails to employees
class Command(BaseCommand):
    def birthday_mails(self, **options):
        today = timezone.now().date()
        for employee in Employee.objects.filter(dob__day=today.day, dob__month=today.month):
            subject = f'Happy Birthday {employee.first_name} {employee.last_name}'
            message = f'Hello {employee.first_name},\n\nWishing you a very happy birthday!'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [employee.email]
            send_mail(subject, message, from_email, recipient_list)