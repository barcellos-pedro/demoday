from django.db import models

# Create your models here.
class FaleAqui(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    assunto = models.CharField(max_length=100)
    mensagem = models.TextField(max_length=300)

    def __str__(self):
        return "E-mail: "+ self.email + " | Assunto: "+ self.assunto

class Faculdade(models.Model):
    nome = models.CharField(max_length=300)

    def __str__(self):
        return self.nome

class aluno(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=12)
    rg = models.CharField(max_length=10)
    dt_Nascimento = models.DateField()
    email = models.EmailField()

