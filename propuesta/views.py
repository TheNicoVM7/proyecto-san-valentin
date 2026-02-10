from django.shortcuts import render

# Create your views here.
def propuesta(request):
    return render(request, 'propuesta/propuesta.html')

def exito(request):
    return render(request, 'propuesta/exito.html')