from django.shortcuts import render, redirect
import datetime

from .forms import TransacaoForm
from .models import Transacao


# Exemplo sem banco de dados
def home(request):
    data = {}
    data['Transacao'] = ['t1', 't2', 't3', 't4', 't5']
    data['now'] = datetime.datetime.now()
    return render(request, 'contas/home.html', data)

# Página de listagem
def listagem(request):
    data = {}
    data['Transacao'] = Transacao.objects.all()
    return render(request, 'contas/listagem.html', data)

def nova_transacao(request):
    data = {}
    form = TransacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    data['form'] = form
    return render(request, 'contas/form.html', data)

def update(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    form = transacaoform = TransacaoForm(request.POST or None, instance=transacao)

    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    data={}
    data['form'] = form
    data['obj'] = transacao
    return render(request, 'contas/form.html', data)

def delete(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    transacao.delete()

    return redirect('url_listagem')



