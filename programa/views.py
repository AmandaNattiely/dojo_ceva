from django.shortcuts import render, HttpResponseRedirect
from programa.models import Cerveja


def index(request):
    cervejas = Cerveja.objects.all()
    return render(request, 'index.html', {'cervejas':cervejas})

def cervejaAdicionar(request):
    return render(request, 'form.html')

def cervejaSalvar(request):
    if request.method == 'POST':
        codigo = request.POST.get('codigo', '0')

        cerveja = Cerveja()
        cerveja.nome = request.POST.get('nome', '').upper()
        cerveja.preco = request.POST.get('preco', '0.00')

        cerveja.save()

    return HttpResponseRedirect('/')
