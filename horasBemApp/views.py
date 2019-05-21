from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from horasBemApp.forms import FaleAquiForm, Login, CadOngForm, CadAlunoForm
from horasBemApp.models import Usuario, FaleAqui, Ong, Aluno

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

def CadOng(request):
    formulario = CadOngForm(request.POST or None)
    formLogin = Login(request.POST or None)
    if formulario.is_valid():
        usuario = formLogin.save()
        ong = formulario.save(commit=False)
        ong.usuario = usuario
        ong.save()
        formulario = CadOngForm()
        redirect('inicioSite')
    contexto = {
        'form':formulario,
        'login':formLogin
    }
    return render(request,'cadastroOng.html',contexto)

def CadAluno(request):
    formulario = CadAlunoForm(request.POST or None)
    formLogin = Login(request.POST or None)
    if formulario.is_valid():
        usuario = formLogin.save()
        aluno = formulario.save(commit=False)
        aluno.usuario = usuario
        aluno.save()
        formulario = CadAlunoForm()
        redirect('inicioSite')
    contexto = {
        'form':formulario,
        'login':formLogin
    }
    return render(request,'cadastroAluno.html',contexto)

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

        user = Usuario.objects.get(email=email)


        if (senha == user.senha):
            return redirect('/entrar_aluno')
        else:
            messages.error(request,"Usuario e senha invalidos")
        return redirect('/login')
    return render(request,'login.html',contexto)
