from django.db import models

class Customers(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    gender = models.CharField(max_length=10)
    username = models.TextField(primary_key=True)
    Email = models.TextField(null=False)
    password = models.TextField(null=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.username} {self.Email}"

