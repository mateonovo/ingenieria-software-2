# Generated by Django 4.0.4 on 2022-06-12 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacunasaplicadas',
            name='lote',
            field=models.CharField(default='', max_length=100, verbose_name='lote'),
        ),
        migrations.AddField(
            model_name='vacunasaplicadas',
            name='observacion',
            field=models.CharField(default=' ', max_length=100, verbose_name='observacion'),
        ),
    ]
