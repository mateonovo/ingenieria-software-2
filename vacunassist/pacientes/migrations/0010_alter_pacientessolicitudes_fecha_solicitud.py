# Generated by Django 4.0.3 on 2022-05-20 23:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0009_alter_pacientessolicitudes_fecha_solicitud'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pacientessolicitudes',
            name='fecha_solicitud',
            field=models.DateField(default=datetime.datetime.today),
        ),
    ]