from django.db import models
from datetime import datetime

# Create your models here.
class Drive(models.Model):
	drive_name = models.CharField(max_length=255)
	drive_date = models.DateTimeField(default=datetime.now)