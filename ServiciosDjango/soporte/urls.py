from django.contrib import admin
from django.urls import path
from soporte import views

urlpatterns = [
    path('', views.home),
    path('servicios/', views.servicios),
    path('crear/', views.crear),
    path('editar/<str:id>', views.editar, name= 'editar'),
    path('eliminar/<str:id>', views.eliminar, name= 'eliminar'),
    path('movimientos/', views.movimientos),
    path('interesados/', views.inter),

]
