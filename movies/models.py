from django.db import models


class Movie(models.Model):
	title = models.CharField(max_length=200)
	genre = models.CharField(max_length=100)
	director = models.CharField(max_length=120)
	publication_year = models.IntegerField()
	synopsis = models.TextField()

	def __str__(self):
		return f"{self.title} - {self.publication_year}"
