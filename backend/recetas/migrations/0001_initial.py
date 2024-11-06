# Generated by Django 5.0.9 on 2024-11-06 07:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categorias', '0001_initial'),
        ('ingredientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('instrucciones', models.TextField()),
                ('tiempo_preparacion', models.PositiveIntegerField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categorias.categoria')),
                ('ingredientes', models.ManyToManyField(to='ingredientes.ingrediente')),
            ],
        ),
    ]