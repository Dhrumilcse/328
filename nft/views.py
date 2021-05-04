from django.shortcuts import render, HttpResponseRedirect, redirect
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .forms import NftForm
from .models import Nft
from django.db.models import Q
from django.contrib.auth.models import User
from .forms import NftForm
from django.contrib.auth.decorators import login_required

# Home Page
class HomePageView(ListView):
    model = Nft
    template_name = 'home.html'
    ordering = ['-publishedAt']

    #Add additional context for user_count
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        user = User.objects.all()
        user_count = len(user)
        context['user_count'] = user_count
        return context

#Profile View
@login_required
def profilePage(request):
    user = User.objects.get(username=request.user)
    user_id = user.id
    object_list = Nft.objects.filter(uploaded_by__id=user_id)
    ordering = ['-publishedAt']
    
    context = {
        'object_list': object_list,
        'user_data': user,
    }
    
    return render(request, 'profile.html', context)

#Upload file view
class UploadNftView(CreateView):
    model = Nft
    form_class = NftForm
    template_name = 'upload.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super(UploadNftView, self).form_valid(form)

#Delete file view
def deleteNftView(request, id):
    obj = Nft.objects.get(id=id)
    if request.method =="POST":
        obj.delete()
        return redirect('profile')

    return render(request, "delete.html")

#Search Result View
class SearchResultsView(ListView):
    model = Nft
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Nft.objects.filter(
            Q(title__icontains=query) | Q(tags__icontains=query)
        )
        return object_list