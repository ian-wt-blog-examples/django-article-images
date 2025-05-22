# core.models.py

from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey('core.Category', on_delete=models.PROTECT)
    tags = models.ManyToManyField('core.Tag')
    content = models.TextField(blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title


class ContentImage(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='content-images')
