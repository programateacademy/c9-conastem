# Generated by Django 4.2.5 on 2023-09-11 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DataBase', '0009_delete_equidad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aprendizajecentrado',
            name='priority_model',
        ),
        migrations.RemoveField(
            model_name='compromisodelacominudad',
            name='priority_model',
        ),
        migrations.RemoveField(
            model_name='convivenciaescolar',
            name='priority_model',
        ),
        migrations.RemoveField(
            model_name='desarrollo_ciudadania_digital',
            name='priority_model',
        ),
        migrations.RemoveField(
            model_name='inclusion_ingenieria_aula',
            name='priority_model',
        ),
        migrations.RemoveField(
            model_name='relacionesconlacominudad',
            name='priority_model',
        ),
        migrations.RemoveField(
            model_name='sostenibilidad_escuelacomunidadypertenencia',
            name='priority_model',
        ),
        migrations.AddField(
            model_name='aprendizajecentrado',
            name='priority',
            field=models.IntegerField(help_text='Ingrese el nivel de prioridad del 1 al 10 para el numeral', null=True),
        ),
        migrations.AddField(
            model_name='compromisodelacominudad',
            name='priority',
            field=models.IntegerField(help_text='Ingrese el nivel de prioridad del 1 al 10 para el numeral', null=True),
        ),
        migrations.AddField(
            model_name='convivenciaescolar',
            name='priority',
            field=models.IntegerField(help_text='Ingrese el nivel de prioridad del 1 al 10 para el numeral', null=True),
        ),
        migrations.AddField(
            model_name='desarrollo_ciudadania_digital',
            name='priority',
            field=models.IntegerField(help_text='Ingrese el nivel de prioridad del 1 al 10 para el numeral', null=True),
        ),
        migrations.AddField(
            model_name='inclusion_ingenieria_aula',
            name='priority',
            field=models.IntegerField(help_text='Ingrese el nivel de prioridad del 1 al 10 para el numeral', null=True),
        ),
        migrations.AddField(
            model_name='relacionesconlacominudad',
            name='priority',
            field=models.IntegerField(help_text='Ingrese el nivel de prioridad del 1 al 10 para el numeral', null=True),
        ),
        migrations.AddField(
            model_name='sostenibilidad_escuelacomunidadypertenencia',
            name='priority',
            field=models.IntegerField(help_text='Ingrese el nivel de prioridad del 1 al 10 para el numeral', null=True),
        ),
    ]
