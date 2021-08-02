from django.forms import ModelForm
from .models import Servicios

# Create the form class.
class ServicioForm(ModelForm):
     class Meta:
         model = Servicios
         fields = ['descripcion', 'precio']