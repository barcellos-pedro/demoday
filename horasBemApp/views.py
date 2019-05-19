from django.shortcuts import render
from horasBemApp.forms import *

# Create your views here.
def index(request):
    formulario = FaleAquiForm(request.POST or None)
    formLogin = Login(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        formulario = FaleAquiForm()

    contexto = {
        'form':formulario,
        'formLogin':formLogin
    }
    return render(request,'index.html', contexto)

## Aluno
def entrarAluno(request):
    return render(request, 'entrar_aluno.html')

def CadAluno(request):
    formulario = CadAlunoForm(request.POST or None)
    if formulario.is_valid():
        if formulario.save():
            redirect('inicioSite')
    contexto = {'form':formulario}
    return render(request,'cadastroAluno.html',contexto)
