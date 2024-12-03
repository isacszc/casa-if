from django.shortcuts import render

def nome(request):
    return render(request, 'nome.html')