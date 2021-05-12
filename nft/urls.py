from django.urls import path, re_path
from .views import HomePageView, UploadNftView, SearchResultsView, profilePage, deleteNftView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('upload/', login_required(UploadNftView.as_view()), name='upload'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('profile/', profilePage , name='profile'),
    path('<id>/delete', deleteNftView, name='delete'),
]