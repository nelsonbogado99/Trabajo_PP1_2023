from django.db import models
from django.utils import timezone

class Empleado(models.Model):
    
    identificador = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=150)
    departamento = models.CharField(max_length=80)
    fecha_inicio = models.DateField(default=timezone.now)
    dias_trabajo = models.CharField(max_length=80)
    
    TURNO_OPCIONES = (
        ('Dia', 'Dia'),
        ('Tarde', 'Tarde'),
        ('Noche', 'Noche'),
    )

    turno = models.CharField(max_length=5, choices=TURNO_OPCIONES)
    horario_entrada = models.TimeField()
    horario_salida = models.TimeField()
    #Nuevo Campo agregado
    activo = models.BooleanField(default=True)
    telefono = models.CharField(max_length=20, blank=True)



class Jornada(models.Model):
    
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    
    MARCACION_OPCIONES  = (
        ('Entrada', 'Entrada'),
        ('Salida', 'Salida'),
    )
    
    tipo_marcacion = models.CharField(max_length=7, choices=MARCACION_OPCIONES)

   