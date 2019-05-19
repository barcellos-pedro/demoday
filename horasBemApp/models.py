from django.db import models

estado_opc = [
    ('AC', 'Acre'), 
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranão'),
    ('MG', 'Minas Gerais'),
    ('MS', 'Mato Grosso do Sul'),
    ('MT', 'Mato Grosso'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PE', 'Pernanbuco'),
    ('PI', 'Piauí'),
    ('PR', 'Paraná'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('RS', 'Rio Grande do Sul'),
    ('SC', 'Santa Catarina'),
    ('SE', 'Sergipe'),
    ('SP', 'São Paulo'),
    ('TO', 'Tocantins')
]

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

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=12)
    rg = models.CharField(max_length=10)
    dt_Nascimento = models.DateField()
    email = models.EmailField()
    faculdade = models.ForeignKey(Faculdade, on_delete=models.CASCADE)
    rua = models.CharField(max_length=140)
    numero = models.IntegerField()
    cep = models.CharField(max_length=10)
    bairro = models.CharField(max_length=45)
    cidade = models.CharField(max_length=45)
    estado = models.CharField(max_length=2, choices=estado_opc)
    foto = models.ImageField(upload_to='',blank=False)

    def __str__(self):
        return self.nome

class Ong(models.Model):
    nome = models.CharField(max_length=45)
    nome_social = models.CharField(max_length=45)
    sigla = models.CharField(max_length=6)
    rua = models.CharField(max_length=140)
    numero = models.IntegerField()
    cep = models.CharField(max_length=10)
    bairro = models.CharField(max_length=45)
    cidade = models.CharField(max_length=45)
    estado = models.CharField(max_length=2, choices=estado_opc)
    foto = models.ImageField(upload_to='')

    def __str__(self):
        return self.nome_social