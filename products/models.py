import random
import os
from django.db import models


# Create your models here.


def get_filename_ext(filepath):
	base_name = os.path.basename(filename)
	name, ext = os.path.splitext(filename)
	return name, ext


def upload_image_path(instance, filename):
	print(instance)
	print(filename)
	new_filename = random.randint()
	name, ext = get_filename_ext(filename)
	final_filename = '{new_filename}{ext}'.format(new_filename= new_filename, ext=ext)
	return 'upload_image_path/{new_filename}/{final_filename}'.format(new_filename=new_filename, final_filename=final_filename)

class Product (models.Model):
	title 			= models.CharField(max_length=120)
	description 	= models.TextField()
	price			= models.DecimalField(decimal_places=2, max_digits=20)
	image 			= models.ImageField(upload_to='products/', null=True, blank=True)





	def __str__(self):
		return self.title
	
	def __unicode__(self):
		return self.title