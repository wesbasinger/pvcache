from django.core.validators import MinValueValidator, MaxValueValidator

from django.db import models

class Geocache(models.Model):
	title = models.TextField(default="None Provided")
	description = models.TextField(default="None provided.")
	latitude = models.FloatField(default=00.000000)
	longitude = models.FloatField(default=00.000000)
	hint = models.TextField(default="None provided.")
	difficulty = models.PositiveIntegerField(default=1,
		validators=
		[MinValueValidator(1), MaxValueValidator(5)])
	
	def dms(self):
		d_lat = int(self.latitude)
		m_lat = int((self.latitude - d_lat) * 60)
		s_lat = round(
			(self.latitude - d_lat - m_lat/60) * 3600, 3)

		d_lon = int(self.longitude)
		m_lon = int((self.longitude - d_lon) * 60)
		s_lon = round(
			(self.longitude - d_lon - m_lon/60) * 3600, 3)

		return "N %s %s' %s\" W %s %s' %s\"" % (d_lat, m_lat, s_lat, d_lon, m_lon, s_lon) 

	
	def __str__(self):
		return self.title

	def publish(self):
		self.save()

class Log(models.Model):
	text = models.TextField(default="None Provided")
	geocache = models.ForeignKey(Geocache, on_delete=models.CASCADE, default=None)

	def __str__(self):
		return self.text
