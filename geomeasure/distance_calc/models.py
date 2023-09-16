from django.db import models


class DistanceCalculation(models.Model):
	place1 = models.CharField(max_length=255)
	place2 = models.CharField(max_length=255)
	distance = models.FloatField()