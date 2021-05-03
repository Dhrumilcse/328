from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Nft(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(null=True,upload_to="nft_uploads/")
    price = models.DecimalField(default=1, max_digits=5, decimal_places=2)
    tags = models.CharField(null=True, max_length=100)
    publishedAt = models.DateTimeField(default=timezone.now)
    uploaded_by = models.ForeignKey(User, db_column="username", on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, default='5')

    def __str__(self):
        return self.title
    