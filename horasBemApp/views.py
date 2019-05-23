from django.contrib import messages
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

def cad_ong(request):
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
    return render(request, 'cadastroOng.html', contexto)

def cad_aluno(request):
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
    return render(request, 'cadastroAluno.html', contexto)


##Criar CadVaga

## Vagas
def vagas(request):
    data = {}
    data['ongs'] = Ong.objects.all()
    data['usuario'] = Aluno.objects.all()
    data['vagas'] = Vaga.objects.all()
    return render(request, 'vagas.html', data)

## Aluno
def entrar_aluno(request,pk):
    data = {}
    data['ongs'] = Ong.objects.all()
    data['usuario'] = Aluno.objects.get(pk=pk)
    return render(request, 'entrar_aluno.html', data)

## ONG
def entrar_ong(request,pk):
    data = {}
    data ['usuario'] = Ong.objects.get(pk=pk)
    data['vagas'] = Vaga.objects.all()
    return render(request, 'entrar_ong.html', data)

##login
def login_user(request):

    form_login = Login(request.POST or None)

    contexto = {
        'form': form_login
    }

    if request.POST:
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        if form_login.is_valid():
            usuario = Usuario.objects.get(email=email)
            if usuario is not None:
                if senha == usuario.senha:
                    try:
                        aluno = Aluno.objects.get(usuario_id=usuario.id)
                        if aluno is not None:
                            return redirect('/entrar_aluno/%s' % aluno.id)
                    except Aluno.DoesNotExist:
                        try:
                            ong = Ong.objects.get(usuario_id=usuario.id)
                            if ong is not None:
                                return redirect('/entrar_ong/%s' % ong.id)
                        except Ong.DoesNotExist:
                            messages.error(request,"Usuario e senha invalidos")
            else:
               messages.error(request, "Usuario e senha invalidos")

    return render(request, 'login.html', contexto)
