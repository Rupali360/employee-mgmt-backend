from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    salary = models.IntegerField()
    department = models.CharField(max_length=50)
    date_joined = models.CharField(max_length=50)
    is_active = models.BooleanField()
    
class Projects(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    status = models.CharField(max_length=50)  # e.g., 'Ongoing', 'Completed'
    created_at = models.DateTimeField(auto_now_add=True)
    manager_id = models.IntegerField(default=None)

class ActivitiesModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(default=None,max_length=255)

