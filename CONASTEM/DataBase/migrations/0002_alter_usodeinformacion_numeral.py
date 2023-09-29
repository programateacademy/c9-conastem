# Generated by Django 4.2.5 on 2023-09-29 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DataBase', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usodeinformacion',
            name='numeral',
            field=models.CharField(choices=[('1500', '1500 - USO DE LA INFORMACIÓN (DATOS)'), ('1510', '1510 - Uso de la información de pruebas estandarizadas estatales, además de otras evaluaciones.'), ('1520', '1520 - Seguimiento riguroso a la información de las evaluaciones formativas.'), ('1530', '1530 - Hay un proyecto de seguimiento del avance del programa con los estudiantes.'), ('1540', '1540 - Existe un plan individual de educación para cada estudiante.'), ('1550', '1550 - Se utilizan sistemas de protección y de seguimiento de la información.'), ('1560', '1560 - Los estudiantes y los padres tienen acceso a información.')], max_length=10000),
        ),
    ]
