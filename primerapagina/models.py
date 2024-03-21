from django.db import models
from django.contrib.auth.models import User

# Create your models here.
OPCIONES_PAGO = [
    ('ef', 'Efectivo'),
    ('ta', 'Tarjeta'),
]

class Orden(models.Model):
    id_de_orden= models.IntegerField()
    nombre = models.CharField(max_length=512)
    correo = models.IntegerField()
    metodo = models.CharField(max_length=2, choices=OPCIONES_PAGO)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario=models.ForeignKey(User, on_delete=models.CASCADE)
