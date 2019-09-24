from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    fname = models.CharField(max_length=35, null=False)
    lname = models.CharField(max_length=35, null=False)
    email = models.EmailField(max_length=40, null=False)
    content = models.TextField(max_length=200, null=False)

    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"id: {self.id}\nName: {self.lname}, {self.fname}\nEmail: {self.email}\nContent: {self.content}"

class PersonalContact(Contact):

    user = models.ForeignKey(User, on_delete=models.CASCADE)