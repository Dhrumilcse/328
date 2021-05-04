from django.urls import path, re_path

from .views import HomePageView, UploadNftView, SearchResultsView
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('upload/', login_required(UploadNftView.as_view()), name='upload'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('profile/', views.profilePage , name='profile'),
    path('<id>/delete', views.deleteNftView, name='delete' ),
]