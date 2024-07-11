from django.db import models

class Employee(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name
