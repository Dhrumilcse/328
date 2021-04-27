from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .forms import NftForm
from .models import Nft
from django.contrib.auth.decorators import login_required

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