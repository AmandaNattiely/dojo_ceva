from django.shortcuts import render
from programa.models import Cerveja

def index(request):
    cervejas = Cerveja.objects.all()
    return render(request, 'index.html', {'cervejas':cervejas})

def cervejaAdicionar(request):
    return render(request, 'form.html')