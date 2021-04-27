from django.urls import path

from .views import HomePageView, UploadNftView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('upload/', UploadNftView.as_view(), name='upload')
]