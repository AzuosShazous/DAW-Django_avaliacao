# Generated by Django 5.1.4 on 2024-12-08 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='forma_conclusao',
            field=models.CharField(default='nada', max_length=100),
        ),
    ]
