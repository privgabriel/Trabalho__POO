from django.contrib import admin
from escola.models import  Aluno, Curso, Matricula, Usuario, Professor


class Professores(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20

admin.site.register(Professor, Professores)
class Usuarios(admin.ModelAdmin):
    list_display = ('id', 'username',)
    list_display_links = ('id', 'username')
    search_fields = ('username',)
    list_per_page = 20

admin.site.register(Usuario, Usuarios)
class Alunos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20

admin.site.register(Aluno, Alunos)


class Cursos(admin.ModelAdmin):
    professor = Professor().fields=['nome']
    list_display = ('id', 'codigo_curso', 'descricao', 'professor')
    list_display_links = ('id', 'codigo_curso')
    search_fields = ('codigo_curso',)

admin.site.register(Curso, Cursos)

class Matriculas(admin.ModelAdmin):
    list_display = ('id', 'aluno', 'curso', 'periodo')
    list_display_links = ('id',)

admin.site.register(Matricula, Matriculas)

# Register your models here.
