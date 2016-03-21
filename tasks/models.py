from django.db import models
from django.utils import timezone

class Task(models.Model):
	title = models.TextField(default='')
	created_date = models.DateTimeField(default=timezone.now)