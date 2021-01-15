from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('three_days/', views.three_days, name='three_days'),
    path('five_days/', views.five_days, name='five_days'),
    path('city_change/', views.city_change, name='city_change'),
]