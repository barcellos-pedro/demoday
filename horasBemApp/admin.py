from django.contrib import admin
from horasBemApp.models import FaleAqui, Aluno, Faculdade, Ong

admin.site.site_title = "Admin Horas do bem"
admin.site.site_header = "Administração Horas do bem"
admin.site.index_title = "Administração do Sistema"

# Register your models here.
admin.site.register(FaleAqui)
admin.site.register(Aluno)
admin.site.register(Faculdade)
admin.site.register(Ong)

# @admin.register(FaleAqui)
# class FaleAquiAdmin(admin.ModelAdmin):
#     list_display = ('nome', 'email')
#     ordering = ('nome')
#     search_fields = ('nome', 'email')

# @admin.register(Aluno)
# class AlunoAdmin(admin.ModelAdmin):
#     list_display = ('nome')
#     ordering = ('nome')
#     search_fields = = ('nome','cpf','rg','estado','faculdade')

# @admin.register(Faculdade)
# class FaculdadeAdmin(admin.ModelAdmin):
#     list_display = ('nome')
#     ordering = ('nome')
#     search_fields = ('nome')
