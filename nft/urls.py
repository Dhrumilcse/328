from django.urls import path, re_path

from .views import HomePageView, UploadNftView, SearchResultsView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('upload/', UploadNftView.as_view(), name='upload'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    # re_path(r'^buy/(?P<id>\d+)/$', buyView , name='buy')
]