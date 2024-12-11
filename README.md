# Avaliação de DAW - Mini Sistema web

Este repositório contém um sistema web referente à atividade de DAW.

# Domínio: orientação de TCC/Estágio

Este sistema foi criado baseado no processo de orientação presente no IFPB - Campus Cajazeiras.

Tal apliacação consta com duas entidades: professor e aluno, de modo que um professor orienta vários alunos, e um aluno é orientado por um único professor (1:n).

# Como executar a aplicação:

1. Antes de tudo crie um ambiente virtual, cujo objetivo é evitar conflitos com o sistema operativo (depedências, módulos, programas, comandos, etc):

```bash
python3 -m venv "nome do ambiente virtual"
```

2. Instalar o Django (dependências):

```bash
pip install django
```
Caso tenha erros com o módulo django, tente instalá-lo no mesmo nível deste repositório clonado no seu sistema de arquivos.

3. Rode o servidor:

```bash
python3 manage.py runserver
```
Caso tenha erros com as entidades, será necessário aplicar as migrações. Para isso, execute:

```bash
python3 manage.py migrate
```


Por fim, crie um superusuário:

```bash
python3 manage.py createsuperuser
```

~Este tutorial de execução está incompleto, uma vez que não fornece suporte a outros sistemas operacionais além do Linux. Ademais, algumas etapas estão com informações incompletas.~
