from django.db import models


class ChatMessage(models.Model):
    room = models.CharField(max_length=64)
    message = models.CharField(max_length=1024)
