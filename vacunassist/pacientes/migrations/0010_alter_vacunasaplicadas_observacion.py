# Generated by Django 4.0.4 on 2022-06-28 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0009_alter_vacunasaplicadas_observacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacunasaplicadas',
            name='observacion',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='observacion'),
        ),
    ]
