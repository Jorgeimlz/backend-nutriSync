# Generated by Django 5.0.9 on 2024-11-09 22:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ingredientes', '0002_ingrediente_descripcion'),
    ]

    operations = [
        migrations.CreateModel(
            name='IngredientesRecetas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingrediente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ingredientes.ingrediente')),
            ],
        ),
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('instrucciones', models.TextField()),
                ('tiempo_preparacion', models.IntegerField()),
                ('ingredientes', models.ManyToManyField(through='recetas.IngredientesRecetas', to='ingredientes.ingrediente')),
            ],
        ),
        migrations.AddField(
            model_name='ingredientesrecetas',
            name='receta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recetas.receta'),
        ),
    ]
