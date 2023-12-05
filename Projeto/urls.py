from django.contrib import admin
from django.urls import path, include
from escola.views import AlunosViewSet, CursosViewSet, MatriculasViewSet, ListaMatriculasAluno, ListaAlunosMatriculados, LoginPage, CreateAccount, UsuariosViewSet, ListaUsuariosSerializer
from rest_framework import routers
from django.views.generic import RedirectView

router = routers.DefaultRouter()
router.register('alunos', AlunosViewSet, basename='Alunos')
router.register('cursos', CursosViewSet, basename='Cursos')
router.register('matriculas', MatriculasViewSet, basename='Matriculas')
router.register('usuarios', UsuariosViewSet, basename='Usuarios')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('login/', LoginPage.as_view(), name='login'),
    path('create_account/', CreateAccount.as_view(), name='create_account'),
    path('aluno/<int:pk>/matriculas/', ListaMatriculasAluno.as_view()),
    path('curso/<int:pk>/matriculas/', ListaAlunosMatriculados.as_view()),
    path('usuario/<int:pk>/usuarios/', ListaUsuariosSerializer),
]
