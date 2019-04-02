from django.db import models
from Shop_Bok.models import Author,Book,Shop

class userID(models.Model):
    title = models.CharField(max_length=200)
