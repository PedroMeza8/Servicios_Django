from django.shortcuts import render
from .models import Servicios, Movimientos

# Create your views here.

def home(request):
    return render(request,'home.html')

def servicios(request):
    listaServicios= Servicios.objects.all()
    print(listaServicios)
    
    return render(request,'servicios.html', context={'servicios':listaServicios}) 

def movimientos(request):
    listaMovimientos= Movimientos.objects.all()
    print(listaMovimientos)
    
    return render(request,'movimientos.html', context={'movimientos':listaMovimientos}) 

def crear(request):
    return render(request,'crear.html')

def editar(request):
    return render(request,'editar.html')           