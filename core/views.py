from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    contexto = { 'titulo': 'Mi primera web en Django',
     'nombres': ['Dark', 'camilo', 'Boby']}
    
    return render(request, 'home.html', contexto)
