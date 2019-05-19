import datetime
from django import forms
from horasBemApp.models import *

class FaleAquiForm(forms.ModelForm):
    email = forms.CharField(label='E-mail')
    class Meta:
        model = FaleAqui
        fields = [
            "nome",
            "email",
            "assunto",
            "mensagem"
        ]

class CadAlunoForm(forms.ModelForm):
    ##dt_Nascimento = forms.DateField(label='Data de Nascimento')
    cpf = forms.CharField(label='CPF')
    rg = forms.CharField(label='RG')
    email = forms.CharField(label='E-mail')
    class Meta:
        model = Aluno
        fields = '__all__'
        widgets = {
            'dt_Nascimento': forms.DateInput(attrs={'type': 'date'})
        }
        