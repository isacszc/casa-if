from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def pag2(request):
    return render(request, 'pagina_2.html')

def pag3(request):
    return render(request, 'pagina_3.html')