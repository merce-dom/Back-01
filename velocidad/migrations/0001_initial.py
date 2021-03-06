# Generated by Django 3.1.7 on 2021-05-27 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('estructura', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ZonaPerfilVelocidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=20)),
                ('rack', models.IntegerField()),
                ('slot', models.IntegerField()),
                ('db', models.IntegerField()),
                ('dw', models.IntegerField()),
                ('zona', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='estructura.zona')),
            ],
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('velocidad', models.FloatField(blank=True, null=True)),
                ('zona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estructura.zona')),
            ],
        ),
    ]
