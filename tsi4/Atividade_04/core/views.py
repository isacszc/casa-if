from django.shortcuts import render

def nome(request):
    nome_usuario = 'Isac'
    return render(request, 'nome.html', {'name':nome_usuario})

def idade(request):
    return render(request, 'idade.html')