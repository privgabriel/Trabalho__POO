from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula, Usuario, Professor
from django.contrib.auth.models import User


class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'


class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__'


class ListaMatriculasAlunoSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']
    def get_periodo(self, obj):
        return obj.get_periodo_display()


class ListaAlunosMatriculadosSerializer(serializers.ModelSerializer):
    aluno_nome = serializers.ReadOnlyField(source= 'aluno.nome')
    class Meta:
        model = Matricula
        fields = ['aluno_nome']

class ListaProfessoresSerializer(serializers.ModelSerializer):
    professor_nome = serializers.ReadOnlyField(source='professor.nome')

    class Meta:
        model = Professor
        fields = ['professor_nome']


class ListaUsuariosSerializer(serializers.ModelSerializer):
    usuario_nome = serializers.ReadOnlyField(source= 'usuario.username')

    class Meta:
        model = Usuario
        fields = ['usuario_nome']