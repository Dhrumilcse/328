from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Nft(models.Model):
    """ Model: Nft 
    
    Fields
    ------
    ID: Default Primaty Key
    Title: Character Field (Max length: 100)
    Image: Image Field (Null: Flase)
    Price: DecimalField (Max digits 5 with 2 decimal places)
    Tags: Character Field (Comma separated, Max length: 100)
    PublishedAt: DateTimeField (Default: timezone.now())
    UploadedBy: ForeignKey (User)
    Quantity: IntegerField (Default: 5, Null: False)
    """
    title = models.CharField(max_length=100)
    image = models.ImageField(null=False,upload_to="nft_uploads/")
    price = models.DecimalField(default=1, max_digits=5, decimal_places=2)
    tags = models.CharField(null=True, max_length=100)
    publishedAt = models.DateTimeField(default=timezone.now)
    uploaded_by = models.ForeignKey(User, db_column="username", on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, default='5')

    def __str__(self):
        return self.title
    