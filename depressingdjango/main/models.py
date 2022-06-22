from django.db import models

# Create your models here.
class product(models.Model):
   
    Nombre = models.CharField(max_length=40)
    Aprobado = models.BooleanField(default=False)
    Presupuesto = models.IntegerField(default=000)
    Creado = models.DateTimeField((""), auto_now=False, auto_now_add=True)
    

    def __str__(self):
        return self.text
