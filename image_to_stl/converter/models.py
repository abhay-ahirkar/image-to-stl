from django.db import models

class Image(models.Model):
    name = models.CharField(max_length=255)
    image_file = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'converter'

class STL(models.Model):
    name = models.CharField(max_length=255)
    stl_file = models.FileField(upload_to='stl/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'converter'
