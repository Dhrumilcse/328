from django.urls import path, re_path

from .views import HomePageView, UploadNftView, SearchResultsView
from . import views

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('upload/', UploadNftView.as_view(), name='upload'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('profile/', views.profilePage , name='profile'),
    path('<id>/delete', views.deleteNftView, name='delete' ),
]