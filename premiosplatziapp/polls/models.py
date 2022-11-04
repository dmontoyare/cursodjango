import datetime

from django.db import models
from django.utils import timezone

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    # Para que cuando el objeto se invoque, se devuelva el valor question_text y no el texto de object raro que saldria por defecto, recordar que el pr imer atributo de todos los metodos de una clase es self
    def __str__(self):
        return self.question_text

    #  Metodo que permite saber si una pregunta es nueva o vieja
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choise_text =models.CharField(max_length=200)
    votes= models.ImageField(default=0)

    def __str__(self):
        return self.choise_text