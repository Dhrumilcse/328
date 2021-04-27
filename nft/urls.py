from django.urls import path, re_path

from .views import HomePageView, UploadNftView, buyView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('upload/', UploadNftView.as_view(), name='upload'),
    re_path(r'^buy/(?P<id>\d+)/$', buyView , name='buy')
]