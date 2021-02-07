from django.db import models

from datetime import date

class Question(models.Model):
    created_at = models.DateField(default=date.today())
    user = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    questions = models.TextField(default='', help_text='As perguntas devem começar com hífen. Ex: - Cidade de origem?')

class Answer(models.Model):
    user = models.CharField(max_length=50)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answered_at = models.DateField(default=date.today())
    answers = models.TextField(default='')
    latitude = models.CharField(max_length=10, default='')
    longitude = models.CharField(max_length=10, default='')
