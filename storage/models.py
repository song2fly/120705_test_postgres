from django.db import models

# Create your models here.
class Picture(models.Model):
    file_id = models.IntegerField(primary_key=True, null=False)
    user_id = models.CharField(max_length=30, null=False)
    created = models.DateTimeField(null=False)
    exif = models.TextField(null=True)
    favorite = models.TextField(null=False)
    simple_name = models.TextField(null=False)
    size = models.IntegerField(null=False)