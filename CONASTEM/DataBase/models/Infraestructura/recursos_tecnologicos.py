from django.db import models
from django.urls import reverse
from ..GeneralModel import GeneralModel

class RecursosTecnologicos(GeneralModel):

    ITEM_CHOICE = [
        ("141","Las necesidades tecnológicas de los estudiantes y el personal se identifican y abordan como parte del diseño del programa"),
        ("142","Las compras de tecnología están completas o incluidas en un presupuesto futuro."),
        ("143","Los profesores y los estudiantes tienen acceso a la solicitud de mantenimiento o apoyo para el uso de la tecnología de instrucción en el aula."),
        ("144","Se utilizan herramientas digitales como medio de comunicación interna y externa sobre actividades del programa STEM."),
        ("145","Se establece uno o varios espacios de creación (Maker Spaces) para fomentar la creatividad y el desarrollo de proyectos."),
    ]
    
    numeral = models.CharField(
        max_length= 10000,
        choices= ITEM_CHOICE
        )

    def __str__(self):
        return self.numeral