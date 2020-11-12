import datetime

from django.db import models


class OrdemDeServico(models.Model):
    nome = models.CharField(verbose_name='Nome', max_length=255)
    tag = models.CharField(max_length=20)
    data_incial = models.DateField(verbose_name='Data de Iníco', default=datetime.date.today)
    data_final = models.DateField(verbose_name='Data Final', default=datetime.date.today)
    descricao = models.TextField(verbose_name='Descrição do Serviço', help_text='Descreva o serviço à ser realizado')

    def __str__(self):
        return f'{self.nome} - {self.tag}'

    class Meta:
        verbose_name = 'Ordem de serviço'
        verbose_name_plural = 'Ordens de Serviços'


class Arvore(models.Model):
    tag = models.CharField(verbose_name='TAG', max_length=255)
    nome = models.CharField(max_length=255)
    nivel = models.CharField(
        default='Planta',
        max_length=50,
        choices=(
            ('Planta', 'Planta'),
            ('Sistema', 'Sistema'),
            ('Equipamento', 'Equipamento'),
            ('Peça', 'Peça'),
        )
    )
    criticidade = models.TextField()
    requisitos = models.TextField(blank=True, null=True)
    descricao = models.TextField(verbose_name='Descriçao', blank=True, null=True)
    fabricante = models.CharField(max_length=255, blank=True, null=True)
    modelo = models.CharField(max_length=255, blank=True, null=True)
    pai = models.CharField(verbose_name='TAG do elemento pai', max_length=255, blank=True, null=True)
    localizacao = models.CharField(verbose_name='Localização', max_length=250, blank=True, null=True)
    link_historico = models.CharField(max_length=255, blank=True, null=True)
    link_pm = models.CharField(max_length=255, blank=True, null=True)
    link_foto = models.ImageField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.tag} - {self.nome}'

    class Meta:
        verbose_name = 'Árvore de Equipamento'
        verbose_name_plural = 'Árvore de Equipamentos'
