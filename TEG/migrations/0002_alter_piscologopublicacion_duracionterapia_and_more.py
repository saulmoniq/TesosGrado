# Generated by Django 4.1 on 2022-12-12 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TEG', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='piscologopublicacion',
            name='duracionTerapia',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='piscologopublicacion',
            name='precio',
            field=models.IntegerField(default=15),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='cedula',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='telefono',
            field=models.IntegerField(default=0),
        ),
    ]