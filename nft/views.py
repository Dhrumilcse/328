from django.shortcuts import render
from django.views.generic import ListView
from .models import Nft

# Create your views here.
class HomePageView(ListView):
    model = Nft
    template_name = 'home.html'