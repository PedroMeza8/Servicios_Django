from django.shortcuts import redirect, render
from .models import Clientes, Servicios, Movimientos, interesados
from django.contrib import messages
from .forms import ServicioForm


# Create your views here.

def home(request):
    return render(request,'home.html')

def servicios(request):
    listaServicios= Servicios.objects.all()
    print(listaServicios)
    print(request.user)
    
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
    formservicio = ServicioForm()
    if request.method == 'POST':
        form = ServicioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/servicios')
        else:
            messages.warning(request, 'Datos invalidos. Vuelva a cargar')
            return redirect('/crear')    

    
    return render(request,'crear.html', {'servicioform': formservicio})

def editar(request, id):
    serv = Servicios.objects.get(id=id)
    formservicio = ServicioForm(instance=serv)
    if request.method == 'POST':
        form = ServicioForm(request.POST, instance=serv)
        if form.is_valid():
            form.save()
            return redirect('/servicios')
        else:
            messages.warning(request, 'Datos invalidos. Vuelva a cargar')
            return redirect('/crear')   

    return render(request,'editar.html', {'formservicio':formservicio}) 

def eliminar(request, id):
    serv = Servicios.objects.get(id=id)
    serv.delete() 
    return redirect ('/servicios') 

def inter(request):
    mail= request.POST.get('form1')
    interesados.objects.create(mail=mail)
   

    return redirect('/')

