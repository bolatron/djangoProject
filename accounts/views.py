from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator

from .models import Account
from .forms import AccountModelForm

import urllib.request
import json
from random import randint

# -----------------------------------------------------------------------------
# Função que executa a tela e o sistema de registramento de novas pessoas.
def register(request):

    form = AccountModelForm(request.POST or None)
    context = {'form': form}

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/home')
    
    return render(request, 'accounts/register.html', context)

# -----------------------------------------------------------------------------
# Função que cuida da paginação e listagem dos cadastros salvos no sistema.
def cadaster_list(request):

    # Retorna todos os objetos salvos no banco de dados, e ordena eles pelo nome 
    # de forma crescente.
    accounts_list = Account.objects.all().order_by('first_name')

    # Cria a paginação.
    # Neste caso são selecionados 10 itens por página.
    paginator = Paginator(accounts_list, 10)
    page = request.GET.get('page')

    accounts = paginator.get_page(page)

    return render(request, 'accounts/cadaster_list.html', {'accounts': accounts})

# -----------------------------------------------------------------------------
# Função que cuida da edição dos dados de cada cadastro.
def editAccount(request, id):

    # Retorna um objeto com base em seu id, caso ocorra algum erro é retornado
    # um erro 404.
    acc = get_object_or_404(Account, pk=id)

    # Gera um formulário para ser sobreescrito.
    form = AccountModelForm(instance=acc)
    context = {'form': form, 'account': acc}

    if (request.method == 'POST'):
        form = AccountModelForm(request.POST, instance=acc)

        # Caso as informações enviadas sejam válidas o novo formulário é salvo. 
        if(form.is_valid()):
            form.save()
            return redirect('/home')
        else:
            return render(request, 'accounts/edit_account.html', context)
    else:
        return render(request, 'accounts/edit_account.html', context)

# -----------------------------------------------------------------------------
# Função que gera novos cadastros aleatórios.
# Demora um tempo considerável para terminar de executar.
def create_accounts(request):

    for i in range(5):

        # Pega os dados da api que gera nomes aleatórios.
        # É utilizado a biblioteca urllib do Python para isso.
        fhandle = urllib.request.urlopen('https://gerador-nomes.herokuapp.com/nome/aleatorio')

        # Transforma os dados lidos em um objeto no formato JSON.
        data = json.loads(fhandle.read())

        # Cria um novo modelo 'Account' a partir dos dados lidos.
        # O campo nome é será o primeiro nome e o nome do meio;
        # O campo sobrenome será o último nome;
        # O campo idade será uma idade entre 18 e 65 anos;
        # O campo data de nascimento será uma data aleatória (deve ser corrigida!);
        # O campo email é um email formado com o primeiro nome e o último nome.
        a = Account(
            first_name = data[0] + ' ' + data[1], 
            last_name = data[2], 
            age= str(randint(18, 65)), 
            birth_date = str(randint(1955, 2001)) + '-' + str(randint(10, 12)) + '-' + str(randint(10, 30)), 
            email= data[0] + data[2] + '@email.com'
        )
        a.save()

    return redirect('/home')

# -----------------------------------------------------------------------------
# Função que deleta dados cadastrados no sistemas a partir do id do cadastro.
def deleteAccount(request, id):
    acc = get_object_or_404(Account, pk=id)
    acc.delete()

    return redirect('/home')