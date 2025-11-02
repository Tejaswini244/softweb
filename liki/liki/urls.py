from django.contrib import admin
from django.urls import path
from softapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('chefs/', views.chefs, name='chefs'),
    path('contact/', views.contact, name='contact'),
]