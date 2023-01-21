# Generated by Django 4.1 on 2023-01-20 18:21

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('TEG', '0009_remove_usuario_cedula_remove_usuario_citas_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='email',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='password',
        ),
        migrations.AddField(
            model_name='usuario',
            name='cedula',
            field=models.IntegerField(default=0, verbose_name='Cédula'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='citas',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TEG.citas'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='correo',
            field=models.CharField(default='sample@gmail.com', max_length=50, verbose_name='Correo'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='fechaNacimiento',
            field=models.DateTimeField(default='none', verbose_name='Fecha de nacimiento'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='passActual',
            field=models.CharField(default=12345, max_length=20, verbose_name='Contraseña'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='telefono',
            field=models.IntegerField(default=0, verbose_name='Teléfono'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='tipoDeUsuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TEG.tipodeusuario', verbose_name='Tipo de usuario'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='ubicacion',
            field=models.CharField(default=django.utils.timezone.now, max_length=10, verbose_name='Ubicación'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='username',
            field=models.CharField(max_length=50, verbose_name='Nombre de usuario'),
        ),
    ]
