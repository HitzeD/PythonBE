from django.db import models
from uuid import uuid4

# Create your models here.

class Contact(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    fname = models.CharField(max_length=35)
    lname = models.CharField(max_length=35)
    title = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=200)
