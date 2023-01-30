# Generated by Django 4.1 on 2023-01-29 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TEG', '0002_remove_piscologopublicacion_idusuario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='piscologopublicacion',
            name='duracionTerapia',
            field=models.IntegerField(default=1, verbose_name='Duración de terapia'),
        ),
        migrations.AlterField(
            model_name='piscologopublicacion',
            name='precio',
            field=models.IntegerField(default=15, verbose_name='Precio'),
        ),
    ]