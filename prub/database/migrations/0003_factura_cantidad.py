# Generated by Django 4.0.6 on 2022-08-03 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_factura_apellido_factura_ciudad_factura_correo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='factura',
            name='cantidad',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
