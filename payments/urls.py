from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^buy/(?P<id>\d+)/$', views.buyView , name='buy'),
    path('config/', views.stripe_config, name='config'),
    path('create-checkout-session/', views.create_checkout_session, name='create-checkout-session'),
    path('success/', views.SuccessView.as_view(), name='success'),
    path('cancelled/', views.CancelledView.as_view(), name='cancelled'),
]