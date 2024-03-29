# Generated by Django 4.1 on 2023-01-18 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TEG', '0008_alter_usuario_cedula_alter_usuario_correo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='cedula',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='citas',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='correo',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='fechaNacimiento',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='passActual',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='telefono',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='tipoDeUsuario',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='ubicacion',
        ),
        migrations.AddField(
            model_name='usuario',
            name='email',
            field=models.CharField(default='test@ejemplo.com', max_length=50, verbose_name='email'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='last_login',
            field=models.CharField(default='yesterday', max_length=20, verbose_name='contraseña'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='password',
            field=models.CharField(default='yesterday', max_length=20, verbose_name='contraseña'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='username',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]
