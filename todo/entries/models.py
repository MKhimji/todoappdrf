from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Entry(models.Model):
    date_posted = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    body = models.TextField()
    author = models.ForeignKey('auth.User', related_name='entries', on_delete=models.CASCADE)
    def __str__(self):
        return "%s %s %s %s" %(self.title, self.author.username, self.author.first_name, self.author.last_name)

