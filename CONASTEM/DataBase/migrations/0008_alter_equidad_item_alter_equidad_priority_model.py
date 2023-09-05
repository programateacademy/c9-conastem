# Generated by Django 4.2.5 on 2023-09-05 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DataBase', '0007_alter_criterio_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equidad',
            name='item',
            field=models.CharField(choices=[(' ', 'Todos los estudiantes reciben acceso equitativo a la formación y a los programas. No se selecciona únicamente a los estudiantes con gusto por las asignaturas S.T.E.M., todos los estudiantes hacen parte del programa'), (' ', 'Todos los estudiantes con necesidades específicas e identificadas están siendo ubicados para facilitar su adaptación. Aprendizaje individualizado.'), (' ', 'Se han diseñado acciones o planes especiales para alentar a los estudiantes con bajo interés o desempeño a desarrollar interés en las carreras STEM.'), (' ', 'Los docentes reciben desarrollo profesional sobre las diferencias culturales y de género para enriquecer la formación.'), (' ', 'El aula STEM se diferencia en ubicar a todos los estudiantes, con una consideración especial hacia todos los grupos geográficos, socioeconómicos, raciales, étnicos y de género.'), (' ', 'La institución está preparada para proveer una formación incluyente. Promueve las oportunidades de aprendizaje para todos los estudiantes, pero respeta las diferencias culturales y de género.')], max_length=1000, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='equidad',
            name='priority_model',
            field=models.CharField(choices=[(' ', 'Exploratorio'), (' ', 'Introductorio'), ('', 'Inmerción parcial'), (' ', 'Inmerción completa')], default='Introductorio', max_length=4),
        ),
    ]
