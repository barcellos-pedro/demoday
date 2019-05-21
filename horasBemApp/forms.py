import datetime
from django import forms

from horasBemApp.models import Usuarios, FaleAqui, Aluno, Ong

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

class Login(forms.ModelForm):
    email = forms.EmailField(label="E-mail")
    senha = forms.CharField(label="Senha", widget=forms.PasswordInput)
    class Meta:
        model = Usuarios
        fields = '__all__'

class CadAlunoForm(forms.ModelForm):
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
            'cep',
            'bairro',
            'cidade',
            'estado',
            'foto'
        ]

class CadOngForm(forms.ModelForm):
    class Meta:
        model = Ong
        fields = [
            "nome",
            "nome_social",
            "sigla",
            "rua",
            "numero",
            "cep",
            "bairro",
            "cidade",
            "estado"
        ]

