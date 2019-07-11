from django.db import models
class Article(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=1000)
    content = models.CharField(max_length=10000)
    