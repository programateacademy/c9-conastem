# Generated by Django 4.2.5 on 2023-09-20 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DataBase', '0002_ambienteescolar_code_desarrollodeequiposlideres_code_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ambienteescolar',
            name='code',
        ),
        migrations.RemoveField(
            model_name='ambienteescolar',
            name='sub_numeral',
        ),
        migrations.RemoveField(
            model_name='desarrollodeequiposlideres',
            name='code',
        ),
        migrations.RemoveField(
            model_name='equidad',
            name='code',
        ),
        migrations.RemoveField(
            model_name='equidad',
            name='sub_numeral',
        ),
        migrations.RemoveField(
            model_name='planeacioninstitucional',
            name='code',
        ),
        migrations.RemoveField(
            model_name='recursostecnologicos',
            name='code',
        ),
        migrations.RemoveField(
            model_name='sostenibilidad',
            name='code',
        ),
        migrations.RemoveField(
            model_name='usodeinformacion',
            name='code',
        ),
        migrations.AddField(
            model_name='ambienteescolar',
            name='codigo',
            field=models.CharField(default='1300', max_length=7),
        ),
        migrations.AddField(
            model_name='desarrollodeequiposlideres',
            name='codigo',
            field=models.CharField(default='1000', max_length=7),
        ),
        migrations.AddField(
            model_name='equidad',
            name='codigo',
            field=models.CharField(default='1600', max_length=7),
        ),
        migrations.AddField(
            model_name='planeacioninstitucional',
            name='codigo',
            field=models.CharField(default='1200', max_length=7),
        ),
        migrations.AddField(
            model_name='recursostecnologicos',
            name='codigo',
            field=models.CharField(default='1400', max_length=7),
        ),
        migrations.AddField(
            model_name='sostenibilidad',
            name='codigo',
            field=models.CharField(default='1700', max_length=7),
        ),
        migrations.AddField(
            model_name='usodeinformacion',
            name='codigo',
            field=models.CharField(default='1500', max_length=7),
        ),
        migrations.AlterField(
            model_name='ambienteescolar',
            name='numeral',
            field=models.CharField(choices=[('1300', '1300 - Ambiente escolar'), ('1310', '1310 - Aulas colaborativas donde los docentes comparten la autoridad con los estudiantes de maneras muy específicas.'), ('1320', '1320 - Aprendizaje Virtual como parte del desarrollo de la auto gestión y el auto desarrollo.'), ('1321', '1321 - Los estudiantes deben desenvolverse bien en el trabajo en equipo de forma virtual.'), ('1330', '1330 - La distribución de los salones de clase facilita la integración de asignaturas.'), ('1340', '1340 - Una cultura de investigación y creatividad.'), ('1350', '1350 - Desarrollo de las habilidades del Siglo XXI en cada clase.'), ('1360', '1360 - Autonomía del estudiante es parte del diseño institucional.'), ('1361', '1361 - El acceso al colegio debe ofrecerse durante todo el día.'), ('1362', '1362 - Los estudiantes tienen tiempo disponible para realizar investigación y consultas a docentes.')], max_length=10000),
        ),
        migrations.AlterField(
            model_name='desarrollodeequiposlideres',
            name='numeral',
            field=models.CharField(choices=[('1000', '1000 - Infraestructura'), ('1100', '1100 - Desarrollo de equipos lideres'), ('1110', '1110 - El equipo de liderazgo de educación STEM está definido y nombrado en la institución para establecer monitorear y evaluar el programa completo.'), ('1120', '1120 - Los equipos de docentes abordan las expectativas específicas del programa establecido por el equipo líder.'), ('1130', '1130 - El equipo líder se reúne regularmente para discutir investigaciones, mejores prácticas, éxitos y oportunidades de mejora hacia los objetivos del Programa en Educación STEM.'), ('1140', '1140 - La toma de decisiones es realizada por todo el personal de la institución, el aula y los docentes de áreas especiales.'), ('1150', '1150 - El equipo líder establece un proceso de evaluación del Programa en Educación STEM de forma anual para medir los avances en los diferentes aspectos que componen esta transformación.')], max_length=10000),
        ),
        migrations.AlterField(
            model_name='equidad',
            name='numeral',
            field=models.CharField(choices=[('1600', '1600 - Equidad'), ('1610', '1610 - Todos los estudiantes reciben acceso equitativo a la formación y a los programas. No se selecciona únicamente a los estudiantes con gusto por las asignaturas S.T.E.M., todos los estudiantes hacen parte del programa.'), ('1620', '1620 - Todos los estudiantes con necesidades específicas e identificadas están siendo ubicados para facilitar su adaptación. Aprendizaje individualizado.'), ('1630', '1630 - Se han diseñado acciones o planes especiales para alentar a los estudiantes con bajo interés o desempeño a desarrollar interés en las carreras STEM.'), ('1640', '1640 - Los docentes reciben desarrollo profesional sobre las diferencias culturales y de género para enriquecer la formación.'), ('1650', '1650 - El aula STEM se diferencia en ubicar a todos los estudiantes, con una consideración especial hacia todos los grupos geográficos, socioeconómicos, raciales, étnicos y de género.'), ('1660', '1660 - La institución está preparada para proveer una formación incluyente. Promueve las oportunidades de aprendizaje para todos los estudiantes, pero respeta las diferencias culturales y de género.'), ('1661', '1661 - Procesos claros desarrollados para la inducción de nuevos estudiantes.'), ('1662', '1662 - Programa o actividades que garanticen una transición efectiva para los estudiantes.'), ('1663', '1663 - La educación STEM es incluyente, y una forma importante es hacer que se sientan como en casa a través de actividades o de programas, con suficiente anterioridad para que puedan participar en la labor académica, no como extraños sino ya apropiados de las costumbres de los estudiantes veteranos.'), ('1664', '1664 - La institución tiene por objetivo incrementar la participación de la mujer en las áreas STEM, de tal manera que la población estudiantil involucrada en el programa sea cada vez mayor.')], max_length=10000),
        ),
        migrations.AlterField(
            model_name='planeacioninstitucional',
            name='numeral',
            field=models.CharField(choices=[('1200', '1200 - Planeacion Intitucional'), ('1210', '1210 - Colaboración entre docentes consistente. La institución auspicia el trabajo colaborativo entre grupos de docentes desde la planeación de unidades y actividades hasta la ejecución en el aula.'), ('1220', '1220 - La Integración entre asignaturas es fundamental para el desarrollo académico. La institución considera fundamental la actividad interdisciplinaria para el Programa en Educación STEM.'), ('1230', '1230 - La organización considera el tiempo suficiente para los proyectos. Se han hecho modificaciones en los horarios y las intensidades horarias de las asignaturas, así como en el currículo para dar espacio a la ejecución de proyectos en los diferentes grados escolares.'), ('1240', '1240 - Hay un Programa en Educación STEM estructurado y en marcha, conducido por el equipo líder y avalado por la dirección de la institución educativa'), ('1250', '1250 - Las directivas de la institución consideran el Programa en Educación STEM como central respecto a la estrategia para los próximos 4 a 6 años.')], max_length=10000),
        ),
        migrations.AlterField(
            model_name='recursostecnologicos',
            name='numeral',
            field=models.CharField(choices=[('1400', '1400 - Recursos Tecnologicos'), ('1410', '1410 - Las necesidades tecnológicas de los estudiantes y el personal se identifican y abordan como parte del diseño del programa'), ('1420', '1420 - Las compras de tecnología están completas o incluidas en un presupuesto futuro.'), ('1430', '1430 - Los profesores y los estudiantes tienen acceso a la solicitud de mantenimiento o apoyo para el uso de la tecnología de instrucción en el aula.'), ('1440', '1440 - Se utilizan herramientas digitales como medio de comunicación interna y externa sobre actividades del programa STEM.'), ('1450', '1450 - Se establece uno o varios espacios de creación (Maker Spaces) para fomentar la creatividad y el desarrollo de proyectos.')], max_length=10000),
        ),
        migrations.AlterField(
            model_name='sostenibilidad',
            name='numeral',
            field=models.CharField(choices=[('1700', '1700 - Sostenibilidad-Infraestructura'), ('1710', '1710 - Se cuenta con un plan de financiación estatal o privado que aporte al programa y cubra por lo menos cinco años del proyecto.'), ('1720', '1720 - El equipo líder cuenta con condiciones laborales y de infraestructura específicas que garantizan la proyección del programa a través de los años.'), ('1730', '1730 - El equipo líder asegura que todas las partes interesadas tengan oportunidades continuas para acceder a la información y aprender sobre la implementación de STEM.'), ('1740', '1740 - El Programa en Educación STEM estableció y monitorea los indicadores de gestión que miden el éxito del programa.'), ('1750', '1750 - El Programa en Educación STEM tiene establecido un proceso de auditoría interna/externa cada dos años.')], max_length=10000),
        ),
        migrations.AlterField(
            model_name='usodeinformacion',
            name='numeral',
            field=models.CharField(choices=[('1500', '1500 - Uso de informacion'), ('1510', '1510 - Uso de la información de pruebas estandarizadas estatales, además de otras evaluaciones.'), ('1520', '1520 - Seguimiento riguroso a la información de las evaluaciones formativas.'), ('1530', '1530 - Hay un proyecto de seguimiento del avance del programa con los estudiantes.'), ('1540', '1540 - Existe un plan individual de educación para cada estudiante.'), ('1550', '1550 - Se utilizan sistemas de protección y de seguimiento de la información.'), ('1560', '1560 - Los estudiantes y los padres tienen acceso a información.')], max_length=10000),
        ),
    ]
