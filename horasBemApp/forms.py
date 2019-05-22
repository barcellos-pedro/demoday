import datetime
from django import forms

from horasBemApp.models import Usuario, FaleAqui, Ong, Aluno, Vaga

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
        model = Usuario
        fields = '__all__'

class CadOngForm(forms.ModelForm):
    class Meta:
        model = Ong
        fields = [
            "nome",
            "sigla",
            "rua",
            "numero",
            "cep",
            "bairro",
            "cidade",
            "estado"
        ]

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
        ]

class CadVagaForm(forms.ModelForm):
    class Meta:
        model = Vaga
        fields = [
            "nome_vaga",
            "detalhes",
            "nome_ong"
        ]