from django.db import models

# Create your models here.
class Contact(models.Model):
    firstname=models.CharField(max_length=120)
    lastname=models.CharField(max_length=120)
    age=models.CharField(max_length=2)
    location=models.CharField(max_length=120)
    email=models.CharField(max_length=120)
    phone=models.CharField(max_length=12)
    desc=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.firstname
