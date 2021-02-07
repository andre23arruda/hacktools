from django import forms
from .models import Question, Answer

class QuestionForms(forms.ModelForm):
    class Meta:
        model = Question
        labels = {
            'user': 'Usuário',
            'created_at': 'Cadastrado em',
            'title': 'Título',
            'questions': 'Perguntas',
        }
        fields = list(labels.keys())
        widgets = {
            'created_at': forms.DateInput(attrs={'class': 'form-control'}),
            'user': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'questions': forms.Textarea(attrs={'class': 'form-control', 'rows': 8}),
        }

    def clean(self):
        return self.cleaned_data


class AnswerForms(forms.ModelForm):
    class Meta:
        model = Answer
        labels = {
            'user': 'Usuário',
        }
        fields = list(labels.keys())
        widgets = {
            'user': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        return self.cleaned_data


class AnswerDetailForms(forms.ModelForm):
    class Meta:
        model = Answer
        labels = {
            'user': 'Usuário',
            'answered_at': 'Respondido em',
            'latitude': 'Latitude',
            'longitude': 'Longitude',
        }
        fields = list(labels.keys())
        widgets = {
            'user': forms.TextInput(attrs={'class': 'form-control', 'disabled': ''}),
            'answered_at': forms.DateInput(attrs={'class': 'form-control', 'disabled': ''}),
            'latitude': forms.TextInput(attrs={'class': 'form-control', 'disabled': ''}),
            'longitude': forms.TextInput(attrs={'class': 'form-control', 'disabled': ''}),
        }