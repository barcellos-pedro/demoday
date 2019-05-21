from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from horasBemApp.forms import FaleAquiForm, CadAlunoForm, Login, CadOngForm
from horasBemApp.models import Usuarios, FaleAqui, Aluno, Ong

# Create your views here.
def index(request):
    formulario = FaleAquiForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        formulario = FaleAquiForm()

    contexto = {
        'form':formulario,
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

##login
def login_user(request):

    formLogin = Login(request.POST or None)

    contexto = {
        'form':formLogin
    }

    if request.POST:
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = Usuarios.objects.get(email=email)


        if (senha == user.senha):
            login(request,user)
            return HttpResponse('Foiiiiii')
        else:
            messages.error(request,"Usuario e senha invalidos")
        return redirect('/login/')
    return render(request,'login.html',contexto)
