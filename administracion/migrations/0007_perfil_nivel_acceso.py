# Generated by Django 3.1.7 on 2021-05-05 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0006_auto_20210504_1813'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='nivel_acceso',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='administracion.nivelacceso'),
        ),
    ]
