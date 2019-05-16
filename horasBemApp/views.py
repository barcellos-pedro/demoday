from django.shortcuts import render
from horasBemApp.forms import FaleAquiForm

# Create your views here.
def index(request):
    return render(request,'index.html')

def faleAqui(request):
    formulario = FaleAquiForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        formulario = FaleAquiForm()

    contexto = {'form':formulario}

    return render(request,'main.html', contexto)