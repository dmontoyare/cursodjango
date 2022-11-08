from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question


'''A continuacion se crean 4 viastas basadas en funciones 
(function base views
clase 21: ademas se incluye en el rtrun, la template correspondiente creada en el archivo de templates


la funcion "render" permite llamar la template deseada, lleva tres parametros
1. request
2. la ruta de la template (compuesta por el nombre de la aplicacion + "/" + el nombre de la plantillla
3. las variables que se desseen enviar hacia la tamplate , en formato de diccionario 
 
'''
def index(request):
    lates_question_list = Question.objects.all()
    return render(request, "polls/index.html", {
        "latest_question_list": lates_question_list
    })


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html",{
        "question": question
    })


def results(request, question_id):
    return HttpResponse(f"Estás viendo los resultados de la pregunta {question_id}")


def vote(request, question_id):
    return HttpResponse(f"Estás votando la pregunta número {question_id}")