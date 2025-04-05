from django.contrib import admin
from .models import Cliente, Colaborador, Horas, Projeto, Servico

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id_cliente', 'nome', 'nif', 'email')
    search_fields = ('nome', 'nif')

@admin.register(Colaborador)
class ColaboradorAdmin(admin.ModelAdmin):
    list_display = ('id_colaborador', 'colaborador', 'funcao', 'email')
    search_fields = ('colaborador', 'funcao')

@admin.register(Horas)
class HorasAdmin(admin.ModelAdmin):
    list_display = ('id_marcacao', 'hora_entrada', 'hora_saida', 'id_colaborador', 'id_cliente', 'id_projeto')
    list_filter = ('id_colaborador', 'id_cliente', 'id_projeto')
    search_fields = ('id_colaborador__colaborador',)

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('id_projeto', 'projeto', 'data_inicio', 'data_conclusao_estimada', 'data_conclusao_real')
    search_fields = ('projeto',)

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('id_servico', 'servico')
    search_fields = ('servico',)
