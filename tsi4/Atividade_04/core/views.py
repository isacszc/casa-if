from django.shortcuts import render

def nome(request):
    return render(request, 'nome.html')

def idade(request):
    return render(request, 'idade.html')