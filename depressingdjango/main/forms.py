from django import forms
from .models import product
from datetime import date

# creating a form
class clienteform(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = product
        
        # specify fields to be used
        fields = [
            "Nombre",
            "Aprobado",
            "Presupuesto",
         
        ]

class tecnicoform(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = product
        
        # specify fields to be used
        fields = [
            "Nombre",
            "Aprobado",
            "Presupuesto",
         
            

        ]

class abogadoform(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = product
        
        # specify fields to be used
        fields = [
            "Nombre",
            "Aprobado",
            "Presupuesto",
         
            

        ]
