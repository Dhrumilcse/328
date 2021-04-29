from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .forms import NftForm
from .models import Nft
from django.db.models import Q

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

class SearchResultsView(ListView):
    model = Nft
    template_name = 'search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Nft.objects.filter(
            Q(title__icontains=query) | Q(tags__icontains=query)
        )
        return object_list