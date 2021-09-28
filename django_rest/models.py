from django.db import models


# Create your models here.
class meterReadings (models.Model):

    ChoicesReadigs = (
        ('Газ' ,'Газ'),
        ('Вода','Вода'),
        ('Свет', 'Свет'),
    )

    house = models.CharField(max_length = 100)
    flat = models.IntegerField()
    choicesMater = models.CharField(max_length = 10, choices = ChoicesReadigs, default = 'Газ')
    metRadings = models.IntegerField()
    #amountRub=models.CharField(max_length = 100)

    #стрококвое предстваление
    def __str___(self):
        return self.house
