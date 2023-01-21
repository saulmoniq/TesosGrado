# Generated by Django 4.1 on 2022-12-14 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TEG', '0005_rename_nombre_tipodeusuario_tipo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historiacontrasena',
            name='passActual',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='passUser',
        ),
        migrations.AddField(
            model_name='historiacontrasena',
            name='passUser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TEG.usuario'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='passActual',
            field=models.CharField(default=12345, max_length=20),
        ),
    ]