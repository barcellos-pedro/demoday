from django.shortcuts import render, redirect
from horasBemApp.forms import FaleAquiForm, CadAlunoForm, Login, CadOngForm
from horasBemApp.models import Usuarios, FaleAqui, Aluno, Ong

# Create your views here.
def index(request):
    formulario = FaleAquiForm(request.POST or None)
    formLogin = Login(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        formulario = FaleAquiForm()

    if formLogin.is_valid():
        formLogin.objects.all()
    contexto = {
        'form':formulario,
        'formLogin':formLogin
    }
    return render(request,'index.html', contexto)

## Aluno
def entrarAluno(request):
    alunos = Aluno.objects.all() #OBJECTS - salva o conjunto de objetos que foram cadastrados
    contexto = {
        'alunos': alunos
    }
    return render(request, 'entrar_aluno.html')

def CadAluno(request):
    formulario = CadAlunoForm(request.POST or None)
    if formulario.is_valid():
        if formulario.save():
            redirect('inicioSite')
    contexto = {'form':formulario}
    return render(request,'cadastroAluno.html',contexto)

def CadOng(request):
    formulario = CadOngForm(request.POST or None)
    if formulario.is_valid():
        if formulario.save():
            redirect('inicioSite')
    contexto = {'form':formulario}
    return render(request,'cadastroOng.html',contexto)

## Vagas
def vagas(request):
    return render(request, 'vagas.html')

