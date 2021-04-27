from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .forms import NftForm
from .models import Nft

# Home Page
class HomePageView(ListView):
    model = Nft
    template_name = 'home.html'

#Upload file view
class UploadNftView(CreateView):
    model = Nft
    form_class = NftForm
    template_name = 'upload.html'
    success_url = reverse_lazy('home')
