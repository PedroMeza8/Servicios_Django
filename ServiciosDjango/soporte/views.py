from django.shortcuts import render
from .models import Clientes, Servicios, Movimientos

# Create your views here.

def home(request):
    return render(request,'home.html')

def servicios(request):
    listaServicios= Servicios.objects.all()
    print(listaServicios)
    
    return render(request,'servicios.html', context={'servicios':listaServicios}) 

def movimientos(request):
    if request.method == 'POST':
        dni = request.POST.get('dni')
        cliente1 = Clientes.objects.get(DNI = dni)
        print(cliente1.DNI, 'Mi dni')
        # resultado= cliente1.movimientos_set.all()
        resultado = Movimientos.objects.filter(cliente__DNI = dni)
        print(resultado)
        return render(request,'movimientos.html', context={'movimientos':resultado})
    listaMovimientos= Movimientos.objects.all()
    print(listaMovimientos)
    
    return render(request,'movimientos.html', context={'movimientos':listaMovimientos}) 

def crear(request):
    return render(request,'crear.html')

def editar(request):
    return render(request,'editar.html')           