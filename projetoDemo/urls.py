"""projetoDemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from horasBemApp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='inicioSite'),
    path('entrar_aluno/<int:pk>/', views.entrar_aluno,name='areaAluno'),
    path('entrar_ong/<int:pk>/', views.entrar_ong,name='areaOng'),
    path('vagas', views.vagas, name='areaVagas'),
    path('cadastroOng', views.cad_ong,name='cadOng'),
    path('cadastroAluno', views.cad_aluno, name="cadAluno"),
    path('login',views.login_user, name='login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
