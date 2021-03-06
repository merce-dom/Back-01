# Generated by Django 3.1.7 on 2021-05-04 15:02

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('estructura', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Carga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.CharField(blank=True, max_length=20, null=True)),
                ('remolque', models.CharField(max_length=20)),
                ('fecha_entrada', models.DateField(default=django.utils.timezone.now)),
                ('hora_entrada', models.TimeField(default=django.utils.timezone.now)),
                ('tara', models.IntegerField()),
                ('destino', models.CharField(blank=True, max_length=50, null=True)),
                ('bruto', models.IntegerField(blank=True, null=True)),
                ('fecha_salida', models.DateTimeField(blank=True, null=True)),
                ('agencia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cargas.agencia')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estructura.empresa')),
            ],
        ),
    ]
