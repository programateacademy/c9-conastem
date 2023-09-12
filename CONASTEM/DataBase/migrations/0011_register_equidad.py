# Generated by Django 4.2.5 on 2023-09-11 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DataBase', '0010_remove_aprendizajecentrado_priority_model_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution_name', models.CharField(help_text='Ingrese el nombre de la institución', max_length=100)),
                ('nit', models.CharField(help_text='Ingrese el NIT de la institución', max_length=10)),
                ('adress', models.CharField(help_text='Ingrese la dirección de la institución', max_length=250)),
                ('institution_responsable', models.CharField(blank=True, help_text='Ingrese el representante de la institución', max_length=50, null=True)),
                ('phone', models.IntegerField(help_text='Ingrese el teléfono de la institución')),
                ('email', models.EmailField(help_text='Ingrese el email principal de la institución', max_length=200)),
                ('model', models.CharField(choices=[('Exploratorio', 'Exploratorio'), ('Introductorio', 'Introductorio'), ('Inmerción parcial', 'Inmerción parcial'), ('Inmerción completa', 'Inmerción completa')], max_length=18)),
            ],
            options={
                'verbose_name': 'Formulario de registro de institucion',
                'verbose_name_plural': 'Formulario de registro de instituciones',
            },
        ),
        migrations.CreateModel(
            name='Equidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.IntegerField(help_text='Ingrese el nivel de prioridad del 1 al 10 para el numeral', null=True)),
                ('dep_responsable', models.CharField(default='Dirección', max_length=30)),
                ('track_year', models.IntegerField(help_text='Ingrese año de seguimiento')),
                ('track_date', models.CharField(help_text='Ingrese fecha de seguimiento', max_length=5)),
                ('internal_auditory_date', models.DateField(blank=True, default='31/01/2000', null=True)),
                ('internal_auditory_obs', models.TextField(blank=True, max_length=1000)),
                ('external_auditory_date', models.DateField(blank=True, default='31/01/2000', null=True)),
                ('external_auditory_obs', models.TextField(blank=True, max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('numeral', models.CharField(choices=[('Todos los estudiantes reciben acceso equitativo a la formación y a los programas. No se selecciona únicamente a los estudiantes con gusto por las asignaturas S.T.E.M., todos los estudiantes hacen parte del programa', '1'), ('Todos los estudiantes con necesidades específicas e identificadas están siendo ubicados para facilitar su adaptación. Aprendizaje individualizado.', '2'), ('Se han diseñado acciones o planes especiales para alentar a los estudiantes con bajo interés o desempeño a desarrollar interés en las carreras STEM.', '3'), ('Los docentes reciben desarrollo profesional sobre las diferencias culturales y de género para enriquecer la formación.', '4'), ('El aula STEM se diferencia en ubicar a todos los estudiantes, con una consideración especial hacia todos los grupos geográficos, socioeconómicos, raciales, étnicos y de género.', '5'), ('La institución está preparada para proveer una formación incluyente. Promueve las oportunidades de aprendizaje para todos los estudiantes, pero respeta las diferencias culturales y de género.', '6')], max_length=1000)),
                ('sub_numeral', models.CharField(default='', max_length=500)),
                ('criterio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='DataBase.criterio')),
                ('person_responsable', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='DataBase.personresponsable')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]