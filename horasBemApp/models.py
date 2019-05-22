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

instituicao_opc = [
    ('MACK', 'Universidade Presbiteriana Mackenzie'),
    ('PUCSP', 'Pontifícia Universidade Católica de São Paulo'),
    ('UMESP', 'Universidade Metodista de São Paulo'),
    ('UNAERP', 'Universidade de Ribeirão Preto'),
    ('UNIMEP', 'Universidade Metodista de Piracicaba'),
    ('UNISA', 'Universidade de Santo Amaro'),
    ('UNISANT ANNA', 'Universidade Sant Anna'),
    ('FEBASP', 'Centro Universitário Belas Artes de São Paulo'),
    ('FMU', 'Centro Universitário das Faculdades Metropolitanas Unidas'),
    ('SENAC', 'Centro Universitário Senac-São Paulo'),
    ('UNASP', 'Centro Universitário Adventista de São Paulo'),
    ('UNISAL', 'Centro Universitário Salesiano de São Paulo'),
    ('BSP', 'Business School São Paulo'),
    ('FGV', 'Fundação Getúlio Vargas'),
    ('ESPM', 'Escola Superior de Propaganda e Marketing'),
    ('FCL', 'Faculdade Cásper Líbero'),
    ('FAPCOM', 'Faculdade Paulus de Comunicação e Tecnologia')
]
# Create your models here.
class Usuario(models.Model):
    email = models.EmailField()
    senha = models.CharField(max_length=36)

    def __str__(self):
        return self.email

class FaleAqui(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    assunto = models.CharField(max_length=100)
    mensagem = models.TextField(max_length=300)

    def __str__(self):
        return "E-mail: "+ self.email + " | Assunto: "+ self.assunto

class Ong(models.Model):
    nome = models.CharField(max_length=50)
    sigla = models.CharField(max_length=6)
    rua = models.CharField(max_length=140)
    numero = models.IntegerField()
    cep = models.CharField(max_length=10)
    bairro = models.CharField(max_length=45)
    cidade = models.CharField(max_length=45)
    estado = models.CharField(max_length=2, choices=estado_opc)
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    def __str__(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=12)
    rg = models.CharField(max_length=10)
    dt_Nascimento = models.DateField()
    Instituicao = models.CharField(max_length=15, choices=instituicao_opc)
    rua = models.CharField(max_length=140)
    numero = models.IntegerField()
    cep = models.CharField(max_length=10)
    bairro = models.CharField(max_length=45)
    cidade = models.CharField(max_length=45)
    estado = models.CharField(max_length=2, choices=estado_opc)
    foto = models.ImageField(upload_to='', null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome

class Vaga(models.Model):
    nome_vaga = models.CharField(max_length=100)
    detalhes = models.CharField(max_length=100)
    nome_ong = models.ForeignKey(Ong, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome_vaga