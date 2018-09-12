from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Blogcontent(models.Model):
	title = models.CharField(max_length=200)
	text = models.TextField()
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

class Aboutme(models.Model):
	text = models.TextField()
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	date_added = models.DateTimeField(auto_now_add=True)

class Img(models.Model):
	pic = models.ImageField(upload_to='img')
	intro = models.TextField(max_length=80)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	date_added = models.DateTimeField(auto_now_add=True)