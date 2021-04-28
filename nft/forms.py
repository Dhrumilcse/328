from django import forms
from .models import Nft

class NftForm(forms.ModelForm):

    class Meta:
        model = Nft
        fields = ['title', 'image',  'price', 'tags']
