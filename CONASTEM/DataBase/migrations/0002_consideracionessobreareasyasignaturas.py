# Generated by Django 4.2.5 on 2023-09-15 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DataBase', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsideracionesSobreAreasYAsignaturas',
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
                ('numeral', models.CharField(choices=[('2.1.1', 'Formas innovadoras de enseñanza y aprendizaje en las áreas y asignaturas')], max_length=10000)),
                ('sub_numeral', models.CharField(choices=[('2.1.1', 'Formas innovadoras de enseñanza y aprendizaje en las áreas y asignaturas')], max_length=10000)),
                ('criterio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='DataBase.criterio')),
                ('person_responsable', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='DataBase.personresponsable')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]