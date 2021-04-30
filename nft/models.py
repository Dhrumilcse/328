from django.db import models
from django.utils import timezone

# Create your models here.
class Nft(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(null=True,upload_to="nft_uploads/")
    price = models.DecimalField(default=1, max_digits=5, decimal_places=2)
    tags = models.CharField(null=True, max_length=100)
    publishedAt = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    