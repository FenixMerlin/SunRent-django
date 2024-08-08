from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import*

mission = DefaultRouter()
mission.register(r'mission', MissionViewSet, basename='mission')

urlpatterns = [
  path('', include(mission.urls)),
]