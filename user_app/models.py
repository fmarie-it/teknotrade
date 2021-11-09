from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class CustomUser(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    # created_at = models.DateTimeField(default = timezone.now)
    # updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "CustomUser"