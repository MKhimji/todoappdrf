from django.db import models
from django.contrib.auth.models import User
from pygments.formatters.html import HtmlFormatter
# Create your models here.

class Entry(models.Model):
    date_posted = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    body = models.TextField()
    # when you delete an auth.User instance, delete all Entry instances related to that user
    author = models.ForeignKey('auth.User', related_name='entries', on_delete=models.CASCADE)
    formatter = models.TextField()
    def __str__(self):
        return "%s %s %s %s" %(self.title, self.author.username, self.author.first_name, self.author.last_name)
    #Tried to find a way to save Entry instance when it is created in HTML format
    #Rather than JSON

    def save(self, *args, **kwargs):
        formatter = HtmlFormatter(body=self.body)
        super(Entry, self).save(*args, **kwargs)
