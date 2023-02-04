from django.db import models

# Create your models here.
default_val = {
    'faculty': 'Engineering',
    'department': 'Information and Comunication Technology',
}

class Students(models.Model):
    name = models.CharField(max_length=250)
    reg_no = models.IntegerField(unique=True, primary_key=True)
    faculty = models.CharField(max_length=250, default=default_val['faculty'])
    department = models.CharField(max_length=250, default=default_val['department'])
    program = models.CharField(max_length=250)
    batch = models.CharField(max_length=10)
    session = models.CharField(max_length=10)
    school = models.CharField(max_length=250)
    college = models.CharField(max_length=250)
    phone_no = models.IntegerField()
    fb_id = models.CharField(max_length=250)
    hometown = models.CharField(max_length=250)
    present_address =  models.CharField(max_length=250, default='')
    in_hall = models.BooleanField()