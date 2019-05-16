from django.db import models

# Create your models here.
class FaleAqui(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    assunto = models.CharField(max_length=100)
    mensagem = models.TextField(max_length=300)

    def __str__(self):
        return "E-mail: "+ self.email + " | Assunto: "+ self.email