from django.shortcuts import render
from programa.models import Cerveja

def index(request):
	return render(request, 'index.html')

def cervejaListar(request):
	cevas = Cerveja.objects.all()

	return render(request, 'cervejas/listaCervejas.html', {'cevas' : cervejas})


def cervejaAdicionar(request):

	return render(request, 'cervejas/listaCervejas.html', {'cevas' : cervejas})