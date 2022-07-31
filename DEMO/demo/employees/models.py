from pickle import TRUE
from django.db import models
from home.models import department #trỏ đến department trong home

# Create your models here.
class employees(models.Model):
    employees_id = models.AutoField(primary_key=True)
    department_id = models.ForeignKey(department,default=None, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=False)
    age = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.employees_id},{self.department_id},{self.name},{self.age}"