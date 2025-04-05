from datetime import datetime, timedelta, timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=512, blank=True, null=True)
    telemovel = models.IntegerField(blank=True, null=True)
    telefone = models.IntegerField(blank=True, null=True)
    nif = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=512, blank=True, null=True)
    morada = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        db_table = 'cliente'


class Colaborador(models.Model):
    id_colaborador = models.AutoField(primary_key=True, blank=False, null=False)
    colaborador = models.CharField(max_length=512, blank=True, null=True)
    funcao = models.CharField(max_length=512, blank=True, null=True)
    telemovel = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=512, blank=True, null=True)
    data_entrada = models.DateTimeField(blank=True, null=True)
    data_saida = models.DateTimeField(blank=True, null=True)
    horas_semanais = models.IntegerField(blank=True, null=True)
    horas_trabalhadas = models.IntegerField(blank=True, null=True)
    horas_trabalhaveis = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'colaborador'


class Horas(models.Model):
    id_marcacao = models.AutoField(primary_key=True)
    hora_entrada = models.DateTimeField(blank=True, null=True)
    hora_saida = models.DateTimeField(blank=True, null=True)
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente')
    id_colaborador = models.ForeignKey(Colaborador, models.DO_NOTHING, db_column='id_colaborador')
    id_servico = models.ForeignKey('Servico', models.DO_NOTHING, db_column='id_servico')
    utilizador = models.ForeignKey(User, models.DO_NOTHING, db_column='id')
    id_projeto = models.ForeignKey('Projeto', models.DO_NOTHING, db_column='id_projeto')

    class Meta:
        db_table = 'horas'


class Projeto(models.Model):
    id_projeto = models.AutoField(primary_key=True, blank=False, null=False)
    projeto = models.CharField(max_length=512, blank=True, null=True)
    data_inicio = models.DateTimeField(blank=True, null=True)
    data_conclusao_estimada = models.DateTimeField(blank=True, null=True)
    data_conclusao_real = models.DateTimeField(blank=True, null=True)
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente')
    id_servico = models.ForeignKey('Servico', models.DO_NOTHING, db_column='id_servico')

    class Meta:
        db_table = 'projeto'


class Servico(models.Model):
    id_servico = models.AutoField(primary_key=True)
    servico = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        db_table = 'servico'
