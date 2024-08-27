from django.db import models

# Create your models here.


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    description = models.IntegerField(default=None)

    def __str__(self):
        return self.image.url
