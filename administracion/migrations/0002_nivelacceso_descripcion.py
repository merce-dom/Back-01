# Generated by Django 3.1.7 on 2021-05-04 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='nivelacceso',
            name='descripcion',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
