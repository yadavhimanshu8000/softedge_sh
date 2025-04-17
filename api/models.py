from django.db import models

# Create your models here.

class COMPANY(models.Model):
    company_Name=models.CharField(max_length=50)
    Location=models.CharField(max_length=50)
    About_company=models.TextField()
    Type=models.CharField(max_length=100,choices=(('IT','IT'),
                                               ('NON IT','NON IT'))
                          )
    date_time=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    
    def __str__(self):
        return self.company_Name
    
class Employee(models.Model):
    employee_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    address=models.TextField(max_length=100)
    phone_no=models.CharField(max_length=10)
    about=models.CharField(max_length=100)
    Employee_position=models.CharField(max_length=100,choices=(('HR','HR'),
                                                ('Manager','Manager'),
                                                ('leader','leader')),
                                       )
    company=models.ForeignKey(COMPANY,on_delete=models.CASCADE)
    
    
