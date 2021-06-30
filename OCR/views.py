from django.shortcuts import render

# Create your views here.

def lista_facturas(request):
    return render(request, 'ocr/lista_facturas.html', {})