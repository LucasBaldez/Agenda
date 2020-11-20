from django.shortcuts import render, get_object_or_404
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

def ver_contato(request, contato_id):
    ##contato = Contato.objects.get(id=contato_id)
    contato = get_object_or_404(Contato,id=contato_id)
    return render(request,'contatos/ver_contato.html', {
        'contato': contato
    })
