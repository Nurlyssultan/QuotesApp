from django.db import models
from django.urls import reverse
# Create your models here.
class QuoteAuthor(models.Model):
    author = models.CharField(max_length=64,unique=True)
    famousFor = models.CharField(max_length=32)
    lifeRange = models.CharField(max_length=64)
    def __str__(self):
        return self.author
    def get_absolute_url(self):
        return reverse('author_detail', kwargs = {'pk' : self.pk})
class QuotePost(models.Model):
    quoteDesription = models.CharField(max_length=128)
    quoteAuthor = models.ForeignKey(QuoteAuthor,on_delete = models.CASCADE,related_name ='quotesOfMan')
    def __str__(self):
        return self.quoteDesription
    def get_absolute_url(self):
        return reverse('detail', kwargs = {'pk' : self.pk})
