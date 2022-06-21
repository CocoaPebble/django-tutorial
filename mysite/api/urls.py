from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('notes/', views.getData, name='notes'),
    path('notes/<str:pk>/', views.getOne, name='note')
]