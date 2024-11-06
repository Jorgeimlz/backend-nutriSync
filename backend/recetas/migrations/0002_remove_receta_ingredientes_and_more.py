# Generated by Django 5.0.9 on 2024-11-06 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receta',
            name='ingredientes',
        ),
        migrations.AlterField(
            model_name='receta',
            name='tiempo_preparacion',
            field=models.DurationField(),
        ),
        migrations.AddField(
            model_name='receta',
            name='ingredientes',
            field=models.JSONField(default=[]),
            preserve_default=False,
        ),
    ]
