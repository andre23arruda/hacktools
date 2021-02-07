from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('create_question', QuestionCreate.as_view(), name='create_question'),
    path('question_list', QuestionList.as_view(), name='question_list'),
    path('answer_list', AnswerList.as_view(), name='answer_list'),
    path('answer_create/<int:question_id>', answer_create, name='answer_create'),
    path('answer_view/<int:answer_id>', answer_view, name='answer_view'),
]