from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('professores/', lista_professores, name='lista_professores'),
    path('professores/criar/', criar_professor, name='criar_professor'),
    path('professores/<int:pk>/atualizar/', atualizar_professor, name='atualizar_professor'),
    path('professores/<int:pk>/deletar/', deletar_professor, name='deletar_professor'),
    path('alunos/', lista_alunos, name='lista_alunos'),
    path('alunos/criar/', criar_aluno, name='criar_aluno'),
    path('alunos/<int:pk>/atualizar/', atualizar_aluno, name='atualizar_aluno'),
    path('alunos/<int:pk>/deletar/', deletar_aluno, name='deletar_aluno'),
]
