from django.db import models
from django.utils import timezone

class Item(models.Model):
	title = models.TextField(default='')
	created_date = models.DateTimeField(default=timezone.now)
