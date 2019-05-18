from django import forms
from horasBemApp.models import *

class FaleAquiForm(forms.ModelForm):
    class Meta:
        model = FaleAqui
        fields = [
            "nome",
            "email",
            "assunto",
            "mensagem"
        ]

class CadAlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = [
            "nome",
            "email"
        ]