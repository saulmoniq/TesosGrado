# Generated by Django 4.1 on 2023-01-31 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TEG', '0005_piscologopublicacion_dias'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diasdisp',
            name='nombre',
        ),
    ]
