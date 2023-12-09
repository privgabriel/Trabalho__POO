from rest_framework import viewsets, generics
from escola.models import Aluno, Curso, Matricula, Usuario
from escola.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasAlunoSerializer, ListaAlunosMatriculadosSerializer, UsuariosSerializer, ListaUsuariosSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User



class LoginPage(View):
    template_name = 'login/index.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if username == '' or password == '':
            return render(request, self.template_name, {'error_message': 'Aguardando preenchimento dos campos'})

        if username == 'admin' and password == 'admin':
            return redirect('/admin/')
        else:
            return render(request, self.template_name, {'error_message': 'Usuário ou senha inválidos'})

class CreateAccount(View):
    template_name = 'createAccount/index.html'

    def get(self, request):
        return render(request, self.template_name)

    def create_user_login(self, request):
        Usuarios.username = request.POST.get('username')
        Usuarios.password = request.POST.get('password')

        if Usuarios.username == '' or Usuarios.password == '':
            return render(request, self.template_name, {'error_message': 'Por favor, preencha todos os campos'})

        if Usuarios.username == Usuarios.password:
            return render(request, self.template_name, {'error_message': 'Usuário não pode ser igual à senha'})

        if Usuarios.objects.filter(username=Usuarios.username).exists():
            return render(request, self.template_name, {'error_message': 'Usuário já cadastrado'})

    def post(self, request):
        return self.create_user_login(request)



class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class UsuariosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""
    queryset = User.objects.all()
    serializer_class = UsuariosSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class CursosViewSet(viewsets.ModelViewSet):
    """Exibitndo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class MatriculasViewSet(viewsets.ModelViewSet):
    """Exibindo todas as matriculas"""
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ListaMatriculasAluno(generics.ListAPIView):
    """Listando as matrículas de um aluno ou aluna"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id= self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasAlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListaAlunosMatriculados(generics.ListAPIView):
    """Listando alunos e alunas matriculados em um curso"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id= self.kwargs['pk'])
        return queryset
    serializer_class = ListaAlunosMatriculadosSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListaUsuarios(generics.ListAPIView):

    def get_queryset(self):
        queryset = User.objects.filter(usuario_id= self.kwargs['pk'])
        return queryset
    serializer_class = ListaUsuariosSerializer
