from django.db import models

# Create your models here.
class image(models.Model):
    pic = models.ImageField( upload_to="uploaded_image" , null=True )
    date = models.DateTimeField( auto_now_add=True)
