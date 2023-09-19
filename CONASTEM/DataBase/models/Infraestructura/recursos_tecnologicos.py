from django.db import models
from django.urls import reverse
from ..GeneralModel import GeneralModel

class RecursosTecnologicos(GeneralModel):

    ITEM_CHOICE = [
        ("1410","Las necesidades tecnológicas de los estudiantes y el personal se identifican y abordan como parte del diseño del programa"),
        ("1420","Las compras de tecnología están completas o incluidas en un presupuesto futuro."),
        ("1430","Los profesores y los estudiantes tienen acceso a la solicitud de mantenimiento o apoyo para el uso de la tecnología de instrucción en el aula."),
        ("1440","Se utilizan herramientas digitales como medio de comunicación interna y externa sobre actividades del programa STEM."),
        ("1450","Se establece uno o varios espacios de creación (Maker Spaces) para fomentar la creatividad y el desarrollo de proyectos."),
    ]
    
    code = models.CharField(max_length=4, default="1410")
    
    numeral = models.CharField(
        max_length= 10000,
        choices= ITEM_CHOICE
        )

    def __str__(self):
        return self.numeral