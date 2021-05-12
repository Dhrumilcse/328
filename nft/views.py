# Models
from .models import Nft
from django.db.models import Q
from django.contrib.auth.models import User

# Views
from django.views.generic import ListView, CreateView

# Forms
from .forms import NftForm

# Misc
from django.urls import reverse_lazy
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth.decorators import login_required

class HomePageView(ListView):
    """ Returns an iterable list of all items from database 
    
    Methods
    -------
    get_context_data(self, **kwargs):
        Returns number of total users
    
    Requirements
    ------------
    (1) from django.views.generic import ListView
    """

    model = Nft
    template_name = 'home.html'
    ordering = ['-publishedAt']

    def get_context_data(self, **kwargs):
        """ Returns number of total users by extending context """

        context = super().get_context_data(**kwargs)
        user = User.objects.all()
        user_count = len(user)
        context['user_count'] = user_count
        return context

@login_required
def profilePage(request):
    """ Returns an iterable list of all authenticated user uploaded items ordered by newest first """

    user = User.objects.get(username=request.user)
    user_id = user.id
    object_list = Nft.objects.filter(uploaded_by__id=user_id)
    ordering = ['-publishedAt']
    
    context = {
        'object_list': object_list,
        'user_data': user,
    }
    
    return render(request, 'profile.html', context)


class UploadNftView(CreateView):
    """ Returns a form to let authenticated user upload new images

    Methods
    -------
    add_user(self, form)
        Add authenticated user to the form if form is validated

    Requirements
    ------------
    (1) from django.views.generic import CreateView
    """

    model = Nft
    form_class = NftForm
    template_name = 'upload.html'
    success_url = reverse_lazy('profile')

    def add_user(self, form):
        """ Add authenticated user to the form if form is validated  """
        form.instance.uploaded_by = self.request.user
        return super(UploadNftView, self).add_user(form)

def deleteNftView(request, id):
    """ Delete Object (given ID) and redirects to confirmation page 
    
    Attributes
    ----------
    id : int
        an id of the object that need to be deleted
    """

    obj = Nft.objects.get(id=id)
    if request.method =="POST":
        obj.delete()
        return redirect('profile')

    return render(request, "delete.html")


class SearchResultsView(ListView):
    """ Returns an iterable list of objects that matches the search query
    
    Methods
    -------
    get_queryset(self, form)
        Returns object list for items that matches search query
    """

    model = Nft
    template_name = 'search_results.html'

    def get_queryset(self):
        """ Returns object list for items that matches search query """
        query = self.request.GET.get('q')
        object_list = Nft.objects.filter(
            Q(title__icontains=query) | Q(tags__icontains=query)
        )
        return object_list