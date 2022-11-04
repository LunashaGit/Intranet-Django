from django.db import models
from base.models import BaseModel
from django.contrib.auth.models import User
# Create your models here.

class Profile(BaseModel):
    user = models.OneToOneField(User , on_delete=models.CASCADE , related_name="profile")
    first_name = models.CharField(max_length=50, null=False, blank=True)
    last_name = models.CharField(max_length=50, null=False, blank=True)
    email = models.EmailField(max_length=254, unique=True, null=False, blank=True)
    password = models.CharField(max_length=50, null=False, blank=True)
