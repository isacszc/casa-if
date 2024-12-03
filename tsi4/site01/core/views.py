from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def pag2(request):
    return render(request, 'seila.html')

def contato(request):
    return render(request, 'contato.html')

def quemsomos(request):
    return render(request, 'quemsomos.html')