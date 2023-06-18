"""
URL configuration for Livreleur project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from datetime import datetime
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from users import views as user_view

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('a propos/', views.about, name='about'),
    path('connection/',lambda request: user_view.loginView(request, title="S'inscrire",year=datetime.now().year),name='login'),
    path('deconnection/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls, name='admin'),
    path('inscription/', lambda request: user_view.registerView(request, title="S'inscrire",year=datetime.now().year), name='register'),
    #path("comptes/", include("django.contrib.auth.urls")),
]
