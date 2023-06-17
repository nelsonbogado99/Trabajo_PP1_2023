# Generated by Django 3.2.12 on 2023-06-17 01:55

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificador', models.IntegerField(unique=True)),
                ('nombre', models.CharField(max_length=150)),
                ('departamento', models.CharField(max_length=80)),
                ('fecha_inicio', models.DateField(default=django.utils.timezone.now)),
                ('dias_trabajo', models.CharField(max_length=80)),
                ('turno', models.CharField(choices=[('Dia', 'Dia'), ('Tarde', 'Tarde'), ('Noche', 'Noche')], max_length=5)),
                ('horario_entrada', models.TimeField()),
                ('horario_salida', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Jornada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('tipo_marcacion', models.CharField(choices=[('Entrada', 'Entrada'), ('Salida', 'Salida')], max_length=7)),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control.empleado')),
            ],
        ),
    ]
