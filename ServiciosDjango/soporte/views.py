from django.shortcuts import render
from .models import Servicios

# Create your views here.

def home(request):
    return render(request,'home.html')

def servicios(request):
    listaServicios= Servicios.objects.all()
    print(listaServicios)
    
    return render(request,'servicios.html', context={'servicios':listaServicios}) 

def crear(request):
    return render(request,'crear.html')

def editar(request):
    return render(request,'editar.html')           