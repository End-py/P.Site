
from django.shortcuts import render
from .models import Produto
from django.http import request


#-------------------#

def index(request):
    produtos = Produto.objects.all()

    context = {
        'produtos': produtos
    }

    return render(request, 'index.html', context)

#-------------------#



#-------------------#

def contato(request):
    return render(request, 'contato.html')

#-------------------#



#-------------------#

def produtos(request):
    prod = Produto.objects.all()

    context = {
        'produto': prod
    }

    return render(request, 'produtos.html', context)


#-------------------#


def produto(request, id):
    produto = Produto.objects.get(id=id)

    context = {
        'produto': produto
    }

    return render(request, 'produto.html', context)

#-------------------#



#-------------------#

def error_404(request, exception):
    return render(request,'404.html', exception)

#-------------------#

def error_500(request):
    return render(request,'500.html')

#-------------------#
