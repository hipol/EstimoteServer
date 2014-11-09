from django.db import models

# Create your models here.

class Datapoint(models.Model):
	date = models.DateTimeField()
	distance = models.FloatField()
	minor = models.IntegerField()
	def __str__(self):
		return str(self.date) + ", " + str(self.distance) + ", " + str(self.minor)

	class Meta:
		ordering = ['date',]