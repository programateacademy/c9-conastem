# Generated by Django 4.2.5 on 2023-09-18 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DataBase', '0004_rename_tecnologiaformacioninstruccion_tecnologiaformacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='SostenibilidadFormacionInstruccion',
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
                ('evidence', models.URLField(blank=True, help_text='Ingrese sus evidencias aquí')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('numeral', models.CharField(choices=[('SOSTENIBILIDAD - FORMACIÓN/INSTRUCCIÓN/EVALUACIÓN', '3900'), ('A través del proceso de evaluación del programa en educación STEM se deberán hacer los cambios o actualizaciones a la instrucción para dar a los estudiantes oportunidades efectivas de aprendizaje.', '3910'), ('Se debe garantizar que los docentes incluyan nuevas actividades con nuevos contextos para los estudiantes. Nuevos contenidos y material curricular deben estar en constante desarrollo.', '3920'), ('Desarrollo de experiencias, eventos o competencias en educación STEM con otras instituciones mantienen vivo el espíritu creativo dentro de la comunidad educativa y promueve nuevos desarrollos novedosos por parte de docentes y estudiantes.', '3930')], max_length=240)),
                ('person_responsable', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='DataBase.personresponsable')),
            ],
            options={
                'verbose_name': 'Sostenibilidad - Formación/Instrucción/Evaluación',
                'verbose_name_plural': 'Sostenibilidad - Formación/Instrucción/Evaluación',
            },
        ),
        migrations.CreateModel(
            name='EleccionCarrera',
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
                ('evidence', models.URLField(blank=True, help_text='Ingrese sus evidencias aquí')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('numeral', models.CharField(choices=[('ELECCIÓN DE CARRERA', '3700'), ('La institución educativa programa y promueve actividades Universitarias tempranas.', '3710'), ('Los estudiantes participan en actividades universitarias tempranas, tales como cursos universitarios.', '3711'), ('Los estudiantes participan en clases universitarias desde los últimos grados de formación escolar.', '3712'), ('Dentro de la planeación de la institución educativa se tienen previsto establecer alianzas con universidades.', '3720'), ('Programar actividades de promoción de carreras de las universidades en el campus del colegio.', '3721'), ('Programar eventos universitarios donde los estudiantes visiten las universidades y conozcan las opciones que ofrecen.', '3722'), ('Establecer y programar cursos universitarios para estudiantes de  los últimos grados, tales como cálculos, físicas, químicas, termodinámica, cursos de herramientas computacionales para diseño y representación gráfica, cursos de impresión 3D, etc.', '3723'), ('Hacer uso del conocimiento de profesionales en universidades para el desarrollo de proyectos académicos de los estudiantes.', '3724'), ('Dentro de la planeación de la institución educativa se tiene previsto establecer alianzas con la industria y la empresa privada', '3730'), ('Establecer y programar visitas de empresas al colegio con el objetivo de mostrar sus productos y procesos a los estudiantes.', '3731'), ('Establecer y programar visitas guiadas de los estudiantes a empresas para conocer de primera mano productos y procesos.', '3732'), ('Hacer uso del conocimiento de profesionales en la empresa privada para el desarrollo de proyectos académicos de los estudiantes.', '3733'), ('Programar charlas y presentaciones de profesionales de las diferentes áreas STEM con el objetivo de mostrarle a los estudiantes su campo de desempeño y los nuevos campos de acción en carreras similares o nuevas.', '3734'), ('Dentro de la planeación de la institución educativa se tiene previsto establecer alianzas con institutos de desarrollo técnico.', '3740'), ('Programar actividades de promoción de carreras de las universidades en el campus del colegio.', '3741'), ('Establecer y programar cursos técnicos para estudiantes de  los últimos grados en áreas de desempeño innovadoras y que estén gestando nuevas áreas de trabajo.', '3742'), ('Hacer uso del conocimiento de profesionales en institutos técnicos para el desarrollo de proyectos académicos de los estudiantes', '3743'), ('El emprendimiento es parte fundamental de las nuevas oportunidades laborales y del futuro de los estudiantes. La institución tiene un programa de emprendimiento asociado al Programa en Educación STEM.', '3750'), ('Las experiencias con expertos externos, así como las experiencias de orden universitario se incluyen dentro del diseño de actividades en educación STEM y no se limita a la educación media.', '3760')], max_length=250)),
                ('person_responsable', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='DataBase.personresponsable')),
            ],
            options={
                'verbose_name': 'Elección de carrera',
                'verbose_name_plural': 'Elección de carrera',
            },
        ),
    ]
