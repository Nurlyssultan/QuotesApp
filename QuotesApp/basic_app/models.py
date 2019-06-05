from django.db import models

# Create your models here.
class QuoteAuthor(models.Model):
    author = models.CharField(max_length=64,unique=True)
    famousFor = models.CharField(max_length=32)
class QuotePost(models.Model):
    dateCreation = models.DateField()
    quoteDesription = models.CharField(max_length=128)
    quoteAuthor = models.ForeignKey(QuoteAuthor,on_delete = models.CASCADE,related_name ='quotesOfMan')
