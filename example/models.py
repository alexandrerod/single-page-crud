from django.db import models

# Create your models here.

class OrdemDeServico(models.Model):
    nome = models.CharField(verbose_name='Nome', max_length=255)
    tag = models.CharField(max_length=20)
    data_incial = models.DateField(verbose_name='Data de Iníco', auto_now=True)
    data_final = models.DateField(verbose_name='Data Final', auto_now=True)
    descricao = models.TextField(verbose_name='Descrição do Serviço', help_text='Descreva o serviço à ser realizado')


    def __str__(self):
        return f'{self.nome} - {self.tag}'

