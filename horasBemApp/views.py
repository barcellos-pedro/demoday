from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from horasBemApp.forms import FaleAquiForm, Login, CadOngForm, CadAlunoForm, CadVagaForm
from horasBemApp.models import Usuario, FaleAqui, Ong, Aluno, Vaga

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


##Criar CadVaga

## Vagas
def vagas(request):
    data = {}
    data['ongs'] = Ong.objects.all()
    data['usuario'] = Aluno.objects.all()
    data['vagas'] = Vaga.objects.all()
    return render(request, 'vagas.html', data)

## Aluno
def entrarAluno(request,pk):
    data = {}
    data['ongs'] = Ong.objects.all()
    data['usuario'] = Aluno.objects.get(pk=pk)
    return render(request, 'entrar_aluno.html', data)

## ONG
def entrarOng(request):
    data = {}
    data['vagas'] = Vaga.objects.all()
    return render(request, 'entrar_ong.html', data)

##login
def login_user(request):

    formLogin = Login(request.POST or None)

    contexto = {
        'form':formLogin
    }
    # if request.POST:
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    if formLogin.is_valid():
        usuario = Usuario.objects.all().get(email=email)
        if usuario is not None:
            if (senha == usuario.senha):
                return redirect('/entrar_aluno/%s' % usuario.id)
            else:
                messages.error(request,"Usuario e senha invalidos")
            return redirect('/login')
        else:
            messages.error(request, "Usuario e senha invalidos")
    return render(request,'login.html',contexto)
