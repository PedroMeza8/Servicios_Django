# Generated by Django 3.2.5 on 2021-08-02 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soporte', '0003_movimientos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicios',
            name='descripcion',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
