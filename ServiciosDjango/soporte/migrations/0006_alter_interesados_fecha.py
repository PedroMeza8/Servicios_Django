# Generated by Django 3.2.5 on 2021-08-05 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soporte', '0005_interesados'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interesados',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]