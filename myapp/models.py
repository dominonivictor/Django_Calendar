from django.db import models
from django.contrib.auth.models import User

class Entry(models.Model):
    '''Creates an object with: name, author, date, description and created attributes'''
    #The Entry object will have the basic atributes of an Event on the calendar
    name = models.CharField(max_length=100)#limiting the event name to 100 chars
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} {}'.format(self.name, self.date)
