# Generated by Django 4.1 on 2023-01-31 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TEG', '0011_alter_piscologopublicacion_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='piscologopublicacion',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TEG.usuarioinfo'),
        ),
    ]
