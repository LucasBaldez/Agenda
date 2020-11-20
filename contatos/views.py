from django.shortcuts import render
from .models import Contato


def index(request):
    if request.method=='POST':
        contatos_nome = request.POST.get('nome')
        search_contatos = Contato.objects.filter(nome__icontains = contatos_nome)
        return render(request, 'contatos/index.html', {
            'contatos': search_contatos
        })
    else:
        contatos = Contato.objects.all()
        return render(request, 'contatos/index.html', {
        'contatos': contatos
        })