from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

faculties = [
        ('Engineering', 'Engineering'),
]

departments = [
        ('ICT', 'Information and Communication Technology'),
]

programs = [
        ('IoT', 'Internet of Things'),
]

# Create your models here.


class Students(models.Model):
    name = models.CharField(max_length=250)
    student_id = models.IntegerField(unique=True, primary_key=True)
    faculty = models.CharField(max_length=20, choices=faculties)
    department = models.CharField(max_length=20, choices=departments)
    program = models.CharField(max_length=20, choices=programs)
    batch = models.IntegerField()
    session = models.CharField(max_length=10)
    school = models.CharField(max_length=250)
    college = models.CharField(max_length=250)
    phone_no = PhoneNumberField(blank=False, null=False, unique=True)
    fb_id = models.CharField(max_length=250, blank=True, null=True)
    hometown = models.CharField(max_length=250, blank=False)
    present_address = models.CharField(max_length=250, default='', blank=True)
    in_hall = models.BooleanField(blank=False)
