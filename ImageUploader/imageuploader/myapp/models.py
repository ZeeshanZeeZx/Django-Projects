from django.db import models

class Image(models.Model):
    # title = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='myimages')
    date = models.DateTimeField(auto_now_add=True)
    # description = models.CharField(max_length=150)
    # price = models.IntegerField()