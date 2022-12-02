from django.shortcuts import render
from .models import Bajos, Baterias, Guitarras
from .forms import BajosForm, GuitarrasForm, BateriasForm

def inicio(request):
    return render(request, "inicio.html", {"mensaje_inicio": "Bienvenido a Casa de Música"})


def agregar_bajos(request):
    if request.method == "POST":
        form_bajo_info = BajosForm(request.POST)
        if form_bajo_info.is_valid():
            datos = form_bajo_info.cleaned_data
            bajo_nuevo = Bajos(marca = datos["marca"], modelo = datos["modelo"], año_fabricacion = datos["año_fabricacion"], cuerdas = datos["cuerdas"])
            bajo_nuevo.save()
            return render(request, "inicio.html", {"mensaje_inicio": "El instrumento ha sido agregado exitosamente!"})
    else:
        formulario_vacio = BajosForm()
        return render(request, "agregar_bajos.html", {"form_bajo":formulario_vacio})


def agregar_baterias(request):
    if request.method == "POST":
        form_bateria_info = BateriasForm(request.POST)
        if form_bateria_info.is_valid():
            datos = form_bateria_info.cleaned_data
            bata_nueva = Baterias(marca = datos["marca"], modelo = datos["modelo"], año_fabricacion = datos["año_fabricacion"])
            bata_nueva.save()
            return render(request, "inicio.html", {"mensaje_inicio": "El instrumento ha sido agregado exitosamente!"})
    else:
        formulario_vacio = BateriasForm()
        return render(request, "agregar_baterias.html", {"form_bateria":formulario_vacio})    


def agregar_guitarras(request):
    if request.method == "POST":
        form_guitarra_info = GuitarrasForm(request.POST)
        if form_guitarra_info.is_valid():
            datos = form_guitarra_info.cleaned_data
            guitarra_nueva = Guitarras(marca = datos["marca"], modelo = datos["modelo"], año_fabricacion = datos["año_fabricacion"], cuerdas = datos["cuerdas"])
            guitarra_nueva.save()
            return render(request, "inicio.html", {"mensaje_inicio": "El instrumento ha sido agregado exitosamente!"})
    else:
        formulario_vacio = GuitarrasForm()
        return render(request, "agregar_guitarras.html", {"form_guitarra":formulario_vacio})

def busqueda_db(request):
    return render(request, "busqueda_db.html", {"mensaje_busqueda":"Seleccione un instrumento"})

def resultado_busqueda(request):
    if "marca" in request.GET:
        valor_url = request.GET["marca"]
        if valor_url != "*":
            baterias_filtradas = Baterias.objects.filter(marca = valor_url)
            guitarras_filtradas = Guitarras.objects.filter(marca = valor_url)
            bajos_filtrados = Bajos.objects.filter(marca = valor_url)           
        else:
            baterias_filtradas = Baterias.objects.all()
            guitarras_filtradas = Guitarras.objects.all
            bajos_filtrados = Bajos.objects.all
        return render(request, "resultado_busqueda.html", {"baterias_seleccionadas":baterias_filtradas, "guitarras_seleccionadas":guitarras_filtradas, "bajos_seleccionados":bajos_filtrados})
    else:
        return render(request, "AppInstrumento/busqueda_db.html", {"mensaje":"Por favor, ingrese un instrumento"})