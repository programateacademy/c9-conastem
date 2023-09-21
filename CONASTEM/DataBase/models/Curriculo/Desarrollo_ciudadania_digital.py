from django.db import models
from ..GeneralModel import GeneralModel

# 2.3 DESARROLLO DE UNA CIUDADANÍA DIGITAL
class DesarrolloCiudadaniaDigital(GeneralModel):

    ITEM_CHOICE = [
        ('2300', 'DESARROLLO DE UNA CIUDADANÍA DIGITAL'),
        ("231", "Establecimiento de una alfabetización digital como parte del entendimiento y el alcance de los desarrollos dentro de la 4a revolución industrial."),
        ("232", "Integración del mundo real al mundo virtual y su relación con la vida personal y laboral."),
        ("233", "Integración constante de nuevos desarrollos digitales dentro de actividades curriculares."),
        ("234", "Desarrollo de hábitos de aprendizaje continuo sobre nuevas alternativas y soluciones que aparecen dentro del mundo digital con miras al conocimiento crítico como consumidor y productor digital."),
    ]

    numeral = models.CharField(
        max_length=10000, 
        choices=[(choice[0], f"{choice[0]} - {choice[1]}") for choice in ITEM_CHOICE]
    )
    
    codigo = models.CharField(max_length=7, default='3000')
    def save(self, *args, **kwargs):
        for choice in self.ITEM_CHOICE:
            if choice[0] == self.numeral:
                self.codigo = choice[0]
                break
        super(DesarrolloCiudadaniaDigital, self).save(*args, **kwargs)

    def __str__(self):
        return self.numeral
