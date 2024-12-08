from django.contrib import admin
from .models import Professor, Aluno

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'departamento')

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'forma_conclusao', 'professor')
