from django import forms
from horasBemApp.models import FaleAqui

class FaleAquiForm(forms.ModelForm):
    class Meta:
        model = FaleAqui
        fields = [
            "nome",
            "email",
            "assunto",
            "mensagem"
        ]
        