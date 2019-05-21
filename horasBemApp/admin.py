from django.contrib import admin

from horasBemApp.models import Usuario, FaleAqui, Ong, Aluno, Vaga

admin.site.site_title = "Admin Horas do bem"
admin.site.site_header = "Administração Horas do bem"
admin.site.index_title = "Administração do Sistema"

# Register your models here.
admin.site.register(FaleAqui)
admin.site.register(Ong)
admin.site.register(Usuario)
admin.site.register(Aluno)
admin.site.register(Vaga)