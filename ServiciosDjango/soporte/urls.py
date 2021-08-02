from django.contrib import admin
from django.urls import path
from soporte import views

urlpatterns = [
    path('home/', views.home),
    path('servicios/', views.servicios),
    path('crear/', views.crear),
    path('editar/<str:id>', views.editar, name= 'editar'),
    path('movimientos/', views.movimientos)
]
