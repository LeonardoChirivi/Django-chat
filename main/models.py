from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=True)
    usercod = models.ForeignKey(User)

    class Meta:
        db_table = 'messages'
        ordering = ['-date']
