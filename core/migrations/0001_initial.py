# Generated by Django 3.2.22 on 2023-10-21 02:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entidad',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=75)),
                ('logo', models.ImageField(upload_to='static/core/img/Logo Entidad/', verbose_name='LogoArticulo')),
            ],
        ),
        migrations.CreateModel(
            name='Comunicado',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=75)),
                ('detalle', models.CharField(max_length=100)),
                ('detalle_corto', models.CharField(max_length=45)),
                ('tipo', models.CharField(choices=[('S', 'Suspension de actividades'), ('C', 'Suspension de clase'), ('I', 'Informacion')], default='S', max_length=20)),
                ('visible', models.BooleanField()),
                ('fecha_publicacion', models.DateTimeField()),
                ('fecha_ultima_modificacion', models.DateTimeField()),
                ('entidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.entidad')),
            ],
        ),
    ]