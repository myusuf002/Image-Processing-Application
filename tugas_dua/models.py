from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='img/', blank=True, null=True)

    def __str__(self):
        return self.image.url[len("/media/img/"):]

    class Meta:
        verbose_name_plural = "Images"