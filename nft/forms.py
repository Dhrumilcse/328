from django import forms
from .models import Nft

class NftForm(forms.ModelForm):
    """ Returns fields Title, Image, Price, and Tags """
    
    class Meta:
        model = Nft
        fields = ['title', 'image',  'price', 'tags']
