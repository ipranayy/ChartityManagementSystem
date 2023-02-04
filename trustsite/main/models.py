
from django.db import models
class Contact(models.Model):
    name = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}, ({self.email})"
