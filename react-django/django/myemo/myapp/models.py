from django.db import models

class Person(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=16)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    email = models.EmailField()
    phone_number = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    occupation = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
