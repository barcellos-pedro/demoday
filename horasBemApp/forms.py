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
        fields = [
            'nome',
            'cpf',
            'rg',
            'dt_Nascimento',
            'Instituicao',
            'rua',
            'numero',
            'bairro',
            'cep',
            'cidade',
            'estado'
        ]
        widgets = {
            'dt_Nascimento': forms.DateInput(attrs={'type': 'date'})
        }

class Login(forms.ModelForm):
    email = forms.EmailField(label="E-mail")
    senha = forms.CharField(label="Senha", widget=forms.PasswordInput)
    class Meta:
        model = Usuarios
        fields = '__all__'
