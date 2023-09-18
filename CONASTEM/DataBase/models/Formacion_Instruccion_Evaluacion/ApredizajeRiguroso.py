from django.db import models
from ..GeneralModel import GeneralModel


class AprendizajeRiguroso (GeneralModel):

    ITEM_CHOICE = [
        ("Aprendizaje Riguroso","3200"),
        ("Los estudiantes deben enfrentar problemas del mundo real, globales, de su país, región o ciudad, problemas que le son de su diario vivir.","3210"),
        ("Trabajo cognitivo exigente. Los estudiantes utilizan hábitos mentales, llegan a conclusiones basadas en la evidencia, predicen fenómenos y comportamientos, analizan datos, explican y razonan.","3220"),
        ("Conclusiones basadas en la evidencia","3221"),
        ("El estudiante predice fenómenos y comportamientos","3222"),
        ("El estudiante analiza datos","3223"),
        ("El estudiante explica y razona","3224"),
        ("Los estudiantes se involucran en auténticas actividades colaborativas basadas en la investigación","3225"),
        ("Las prácticas de matemáticas se presentan de forma transversal en las actividades de la gran mayoría de las asignaturas","3230"),
        ("Encontrar sentido a los problemas y perseverar en resolverlos","3231"),
        ("Modelar con matemáticas","3232"),
        ("Utilizar estratégicamente herramientas apropiadas","3233"),
        ("Esmerarse por ser preciso","3234"),
        ("Razonar de manera abstracta y cuantitativamente","3235"),
        ("Buscar y hacer uso de estructuras","3236"),
        ("Construir posibles argumentos y criticar el razonamiento de otros","3237"),
        ("Buscar patrones de cálculo y aplicar métodos generales o autónomos","3238"),
        ("Desarrollo en la institución de una cultura de aprendizaje continuo y durante toda la vida. Desarrollo del estudiante como un consumidor crítico, coherente e informado.","3240")
        ]	
	
	
    numeral = models.CharField(
        max_length= 10000,
        choices= ITEM_CHOICE
        )
    codigo =models.CharField(max_length=7, default="3200")
    def __str__(self) :
        return self.numeral