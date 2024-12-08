from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Professor, Aluno

# Create your views here.

def home(request):
    return render(request, 'home.html')


def lista_professores(request):
    professores = Professor.objects.all()
    return render(request, 'lista_professores.html', {'professores': professores})

def criar_professor(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        departamento = request.POST['departamento']
        Professor.objects.create(nome=nome, departamento=departamento)
        return redirect('lista_professores')
    return render(request, 'form_professor.html')

def atualizar_professor(request, pk):
    professor = get_object_or_404(Professor, pk=pk)
    if request.method == 'POST':
        professor.nome = request.POST['nome']
        professor.departamento = request.POST['departamento']
        professor.save()
        return redirect('lista_professores')
    return render(request, 'form_professor.html', {'professor': professor})

def deletar_professor(request, pk):
    professor = get_object_or_404(Professor, pk=pk)
    if request.method == 'POST':
        professor.delete()
        return redirect('lista_professores')
    return render(request, 'confirmar_deletar_professor.html', {'professor': professor})

def lista_alunos(request):
    alunos = Aluno.objects.select_related('professor').all()
    return render(request, 'lista_alunos.html', {'alunos': alunos})

def criar_aluno(request):
    professores = Professor.objects.all()
    
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        forma_conclusao = request.POST['forma_conclusao']
        professor_id = request.POST['professor']
        professor = get_object_or_404(Professor, pk=professor_id)
        Aluno.objects.create(nome=nome, email=email, forma_conclusao=forma_conclusao, professor=professor)
        return redirect('lista_alunos')
    return render(request, 'form_aluno.html', {'professores': professores})

def atualizar_aluno(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    professores = Professor.objects.all()
    if request.method == 'POST':
        aluno.nome = request.POST['nome']
        aluno.email = request.POST['email']
        aluno.forma_conclusao = request.POST['forma_conclusao']
        aluno.professor_id = request.POST['professor']
        aluno.save()
        return redirect('lista_alunos')
    return render(request, 'form_aluno.html', {'aluno': aluno, 'professores': professores})

def deletar_aluno(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method == 'POST':
        aluno.delete()
        return redirect('lista_alunos')
    return render(request, 'confirmar_deletar_aluno.html', {'aluno': aluno})
