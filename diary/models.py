from django.db import models

# Create your models here.


class Page(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    feelings = models.CharField(max_length=80)
    score = models.IntegerField()
    dt_created = models.DateField(
        verbose_name="Date Created")

    def __str__(self):
        return self.title
