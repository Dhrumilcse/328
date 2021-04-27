from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'^buy/(?P<id>\d+)/$', views.buyView , name='buy'),
    path('config/', views.stripe_config),
    path('create-checkout-session/', views.create_checkout_session),
    path('success/', views.SuccessView.as_view()),
    path('cancelled/', views.CancelledView.as_view()),
]