from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('login/', views.signin, name='signin'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
]