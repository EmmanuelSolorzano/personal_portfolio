from django.db import models
import datetime

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=700)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)
    dateProject = models.DateField(default=datetime.date.today)
    youtubeResourceID = models.CharField(blank=True,max_length=500)
    imageResource = models.ImageField(blank=True,upload_to='portfolio/images/')

    def __str__(self):
        return self.title