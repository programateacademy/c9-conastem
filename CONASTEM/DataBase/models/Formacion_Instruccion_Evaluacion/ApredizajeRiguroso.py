from django.db import models
from ..GeneralModel import GeneralModel


class AprendizajeRiguroso (GeneralModel):

    ITEM_CHOICE = [
        ("3200","APRENDIZAJE RIGUROSO"),
        ("3210","Los estudiantes deben enfrentar problemas del mundo real, globales, de su país, región o ciudad, problemas que le son de su diario vivir."),
        ("3220","Trabajo cognitivo exigente. Los estudiantes utilizan hábitos mentales, llegan a conclusiones basadas en la evidencia, predicen fenómenos y comportamientos, analizan datos, explican y razonan."),
        ("3221","Conclusiones basadas en la evidencia"),
        ("3222","El estudiante predice fenómenos y comportamientos"),
        ("3223","El estudiante analiza datos"),
        ("3224","El estudiante explica y razona"),
        ("3225","Los estudiantes se involucran en auténticas actividades colaborativas basadas en la investigación"),
        ("3230","Las prácticas de matemáticas se presentan de forma transversal en las actividades de la gran mayoría de las asignaturas"),
        ("3231","Encontrar sentido a los problemas y perseverar en resolverlos"),
        ("3232","Modelar con matemáticas"),
        ("3233","Utilizar estratégicamente herramientas apropiadas"),
        ("3234","Esmerarse por ser preciso"),
        ("3235","Razonar de manera abstracta y cuantitativamente"),
        ("3236","Buscar y hacer uso de estructuras"),
        ("3237","Construir posibles argumentos y criticar el razonamiento de otros"),
        ("3238","Buscar patrones de cálculo y aplicar métodos generales o autónomos"),
        ("3240","Desarrollo en la institución de una cultura de aprendizaje continuo y durante toda la vida. Desarrollo del estudiante como un consumidor crítico, coherente e informado.")
        ]	
	
	
    numeral = models.CharField(
        max_length= 10000,
        choices=[(choice[0], f"{choice[0]} - {choice[1]}") for choice in ITEM_CHOICE]
        )
    codigo =models.CharField(max_length=4)
    def save(self, *args, **kwargs):
        # Buscar el número correspondiente al ítem seleccionado en ITEM_CHOICE
        for choice in self.ITEM_CHOICE:
            if choice[0] == self.numeral:
                self.codigo = choice[0]
                self.numeral = choice[1]
                break

        super(AprendizajeRiguroso, self).save(*args, **kwargs)

    def __str__(self) :
        return self.numeral