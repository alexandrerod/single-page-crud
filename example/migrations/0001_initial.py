# Generated by Django 3.1.3 on 2020-11-05 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrdemDeServico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('tag', models.CharField(max_length=20)),
                ('data_incial', models.DateField(auto_now=True, verbose_name='Data de Iníco')),
                ('data_final', models.DateField(auto_now=True, verbose_name='Data Final')),
                ('descricao', models.TextField(help_text='Descreva o serviço à ser realizado', verbose_name='Descrição do Serviço')),
            ],
        ),
    ]