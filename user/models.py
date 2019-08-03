from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
def get_sentinel_user():
	return get_user_model().objects.get_or_create(username='deleted')[0]

class Post(models.Model):
	title = models.CharField(max_length=100)
	entry = models.TextField()

	created = models.DateTimeField(auto_now=True)
	updated = models.DateTimeField(auto_now=True)

	show_recent = models.BooleanField(default=True)
	pinned = models.BooleanField(default=False)
	locked = models.BooleanField(default=False)
	deleted = models.BooleanField(default=False)

	user = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.SET(get_sentinel_user)
	)

	def __str__(self):
		return '[%s] %s' % (self.user.username,self.title)

class Comment(models.Model):
	entry = models.TextField()

	created = models.DateTimeField(auto_now=True)
	updated = models.DateTimeField(auto_now=True)
	
	deleted = models.BooleanField(default=False)
	
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	user = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.SET(get_sentinel_user)
	)

