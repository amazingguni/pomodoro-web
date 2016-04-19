from django.db import models
from django.utils import timezone

class List(models.Model):
	pass

class Item(models.Model):
	text = models.TextField(default='')
	list = models.ForeignKey(List, default=None)

