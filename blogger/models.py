from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model):
	title = models.CharField(max_length=500)
	content = models.TextField()
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blogs")
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.title

class Comment(models.Model):
	blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
	text = models.CharField(max_length=1000)
	commenter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.text

