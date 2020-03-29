from django.db import models


class Images(models.Model):
	photo = models.Imagefield()

	class Meta
		verbose_name_plural = "Images"

	def __str__(self):
		return self.photo.name
