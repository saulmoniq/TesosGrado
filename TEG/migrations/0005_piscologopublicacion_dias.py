# Generated by Django 4.1 on 2023-01-31 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TEG', '0004_diasdisp'),
    ]

    operations = [
        migrations.AddField(
            model_name='piscologopublicacion',
            name='dias',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TEG.diasdisp'),
        ),
    ]