
from django.contrib import admin
from .models import Produto, Cliente


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')

admin.site.register(Produto, ProdutoAdmin)


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'usuario', 'senha', 'email', 'cpf', 'data_de_nascimento', 'telefone', 'sexo')

admin.site.register(Cliente, ClienteAdmin)

