from django.contrib import admin
from .models import Empleado, Jornada


class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'departamento', 'turno', 'dias_trabajo', 'horario_entrada', 'horario_salida')
    list_filter = ('nombre',)
    ordering = ('-turno',)

class JornadaAdmin(admin.ModelAdmin):
    list_display = ('empleado', 'fecha', 'tipo_marcacion')
    ordering = ('-fecha',)

admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Jornada, JornadaAdmin)

