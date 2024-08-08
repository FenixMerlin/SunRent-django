from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from API.views import*


urlpatterns = [
  path('', views.index, name='index'),
  path('maps/', views.maps, name='maps'),
]