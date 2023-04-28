from django.db import models


class Hotel(models.Model): 
    nombre = models.CharField(max_length=60)
    direccion = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()

class Reserva(models.Model):
    fechaEntrada = models.DateField()
    fechaSalida = models.DateField()
    N_huespedes = models.PositiveBigIntegerField()
    tipoAbitacion = models.CharField(max_length=30)
    precioTotal = models.CharField(max_length=100)
    estadoReserva = models.CharField(max_length=60)