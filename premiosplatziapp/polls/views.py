from django.shortcuts import render
from django.http import HttpResponse
from .models import Question


'''A continuacion se crean 4 viastas basadas en funciones 
(function base views
clase 21: ademas se incluye en el rtrun, la template correspondiente creada en el archivo de templates
'''
def index(request):
    lates_question_list = Question.objects.all()
    return render(request, "polls/index.html", {
        "latest_question_list": lates_question_list
    })


def detail(request, question_id):
    return HttpResponse(f"Estás viendo la pregunta número {question_id}")


def results(request, question_id):
    return HttpResponse(f"Estás viendo los resultados de la pregunta {question_id}")


def vote(request, question_id):
    return HttpResponse(f"Estás votando la pregunta número {question_id}")