from rest_framework import viewsets, generics
from escola.models import Aluno, Curso, Matricula, Usuario, Professor
from escola.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasAlunoSerializer, ListaAlunosMatriculadosSerializer, UsuariosSerializer, ListaUsuariosSerializer, ProfessorSerializer, ListaProfessoresSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User


from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login

class LoginPage(View):
    template_name = 'login/index.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == '' or password == '':
            return render(request, self.template_name, {'error_message': 'Aguardando preenchimento dos campos'})

        # Verificar directamente en el modelo User
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None

        if user is not None and user.check_password(password):
            # Usuario autenticado correctamente
            login(request, user)
            return redirect('/admin/')  # Puedes redirigir a la página principal o a donde desees
        else:
            return render(request, self.template_name, {'error_message': 'Usuário ou senha inválidos'})

class CreateAccount(View):
    template_name = 'createAccount/index.html'

    def get(self, request):
        return render(request, self.template_name)

    def create_user(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            return render(request, self.template_name, {'error_message': 'Por favor, preencha todos os campos'})

        if User.objects.filter(username=username).exists():
            return render(request, self.template_name, {'error_message': 'Nome de usuário já em uso'})

        user = User.objects.create_user(username=username, password=password)
        # Puedes hacer más cosas con el usuario creado, como iniciar sesión automáticamente.

        return redirect('/')  # O redirige a la página que desees después de crear la cuenta

    def post(self, request):
        return self.create_user(request)




class ProfessorViewSet(viewsets.ModelViewSet):
    """Exibindo todos os professores e professoras"""
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

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


class ListaProfessores(generics.ListAPIView):
    """Listando alunos e alunas matriculados em um curso"""
    def get_queryset(self):
        queryset = Professor.objects.filter(id= self.kwargs['pk'])
        return queryset
    serializer_class = ListaProfessoresSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListaUsuarios(generics.ListAPIView):

    def get_queryset(self):
        queryset = User.objects.filter(usuario_id= self.kwargs['pk'])
        return queryset
    serializer_class = ListaUsuariosSerializer
