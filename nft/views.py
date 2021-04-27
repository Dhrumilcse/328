from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .forms import NftForm
from .models import Nft
from django.contrib.auth.decorators import login_required
import requests

# Create your views here.
class HomePageView(ListView):
    model = Nft
    template_name = 'home.html'

# @login_required
class UploadNftView(CreateView):
    model = Nft
    form_class = NftForm
    template_name = 'upload.html'
    success_url = reverse_lazy('home')
    
@login_required
def buyView(request, id):
    nft = Nft.objects.get(id=id)
    # print(nft.title
    # image_url = nft.image.url

    context = {
        'nft': nft
    }

    return render(request, 'buy.html', context)