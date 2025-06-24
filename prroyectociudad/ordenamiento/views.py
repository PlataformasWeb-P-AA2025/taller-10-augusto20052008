from django.shortcuts import render, redirect
from ordenamiento.models import Parroquia, Barrio
from ordenamiento.forms import ParroquiaForm, BarrioForm

def index(request):
    return render(request, 'ordenamiento/index.html')

# Create your views here.
def listar_parroquias_y_barrios(request):
    parroquias = Parroquia.objects.all()
    return render(request, 'ordenamiento/listar_parroquias.html', {'parroquias': parroquias})

def listar_barrios(request):
    barrios = Barrio.objects.all()
    return render(request, 'ordenamiento/listar_barrios.html', {'barrios': barrios})

def crear_parroquia(request):
    if request.method == 'POST':
        form = ParroquiaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(listar_parroquias_y_barrios)
    else:
        form = ParroquiaForm()
    return render(request, 'ordenamiento/crear_parroquia.html', {'form': form})

def crear_barrio(request):
    if request.method == 'POST':
        form = BarrioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(listar_barrios)
    else:
        form = BarrioForm()
    return render(request, 'ordenamiento/crear_barrio.html', {'form': form})
