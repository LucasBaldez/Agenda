from datetime import timezone
from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Contato(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255, blank = True)
    telefone = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank = True)
    data_criacao = models.DateTimeField()
    descricao = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria,on_delete=models.DO_NOTHING)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome



