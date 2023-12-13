from django.contrib import admin
from .models import Endereco, Tutor

# Register your models here.

@admin.register(Endereco)
class EndenrecoAdmin(admin.ModelAdmin):
    list_display = ['cep', 'estado', 'estado', 'complemento']

@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cpf', 'contato', 'email', 'endereco', 'data_de_nascimento', 'data_de_cadastro']
    list_editable = ['endereco',]
