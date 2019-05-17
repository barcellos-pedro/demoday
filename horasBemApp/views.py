from django.shortcuts import render
from horasBemApp.forms import FaleAquiForm

# Create your views here.
def index(request):
    formulario = FaleAquiForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        formulario = FaleAquiForm()

    contexto = {'form':formulario}
    return render(request,'index.html', contexto)

def entrarAluno(request):
    return render(request, 'entrar_aluno.html'  )