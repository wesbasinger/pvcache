from django.db import models

class Geocache(models.Model):
	title = models.TextField(default="None Provided")
	description = models.TextField(default="None provided.")
	latitude = models.FloatField(default=00.000000)
	longitude = models.FloatField(default=00.000000)

	def __str__(self):
		return self.title

class Log(models.Model):
	text = models.TextField(default="None Provided")
	geocache = models.ForeignKey(Geocache, on_delete=models.CASCADE, default=None)

	def __str__(self):
		return self.text
