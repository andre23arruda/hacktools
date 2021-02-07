from django.contrib import admin
from .models import Answer, Question

@admin.register(Question)
class QuestionRegister(admin.ModelAdmin):
    list_display = ['user', 'title']


@admin.register(Answer)
class AnswerRegister(admin.ModelAdmin):
    list_display = ['user', 'question']