from django.db import models

class Geocache(models.Model):
	title = models.TextField(default="None Provided")
	description = models.TextField(default="None provided.")
