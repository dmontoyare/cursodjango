from django.urls import path 
from . import views

'''los corchetes angulares <> para pasar parametros variables mediante la url,
o sea, entre los corchetes se pone el parametro question_id por lo tanto como esto es
una anidacion de polls/ entonces al ingresar al polls/4 o cualuqiern umero de id, se
estaria entrando a la pregunta deseada '''
urlpatterns = [
    #ex polls/
    path("", views.index, name="index"),
    #ex polls/5
    path("<int:question_id>/", views.detail, name="index"),
    #ex polls/5/results
    path("<int:question_id>/results/", views.results, name="index"),
    #ex polls/5/votes
    path("<int:question_id>/vote/", views.vote, name="index"),

]