from django.db import models

# Create your models here.

class Cars(models.Model):
    title = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    image = models.ImageField(upload_to='image')
    phone = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    owner = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'

    def __str__(self) -> str:
        return f'{self.title}'