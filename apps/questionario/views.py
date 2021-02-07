from django.views.generic import (
    CreateView, DetailView, ListView, TemplateView,
    UpdateView
)
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
import json

from .models import Question, Answer
from .forms import QuestionForms, AnswerForms, AnswerDetailForms


class IndexView(TemplateView):
    template_name = "index.html"


class QuestionCreate(SuccessMessageMixin, CreateView):
    model = Question
    form_class = QuestionForms
    template_name = "create_question.html"
    success_url = '/'
    success_message = "Questionário criado com sucesso"


class QuestionList(ListView):
    model = Question
    template_name = "question_list.html"


class AnswerList(ListView):
    model = Answer
    template_name = "answer_list.html"


def answer_create(request, question_id):
    question = Question.objects.get(pk=question_id)
    if request.method == 'POST':
        answer = Answer.objects.create(
            user=request.POST['user'],
            question=question,
            answers=json.loads(request.POST['answers']),
            latitude=request.POST['latitude'],
            longitude=request.POST['longitude'],
        )
        messages.success(request, f'Salvo com sucesso!')
        context = {"status":"success", "message":"success"}
        return HttpResponse(json.dumps(context), content_type='application/json')
    form = AnswerForms()
    questions = question.questions.split('-')
    questions.pop(0)

    context = {
        'question': question,
        'form': form,
        'questions': questions,
    }

    return render(request, 'answer_create.html', context)


def answer_view(request, answer_id):
    answer = Answer.objects.get(pk=answer_id)
    form = AnswerDetailForms(instance=answer)
    questions = answer.question.questions.split('-')
    questions.pop(0)

    context = {
        'answer': answer,
        'form': form,
        'questions': questions,
    }

    return render(request, 'answer_detail.html', context)
