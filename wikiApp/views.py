from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import articulo,tema

# Create your views here.
def vistaPrincipal(request):
    return render(request,'vistaPrincipal.html',{
        'temasSistema':tema.objects.all()
    })

def nuevoArticulo(request):
    if request.method == 'POST':
        tituloArticulo = request.POST.get('tituloArticulo')
        descripcionArticulo = request.POST.get('descripcionArticulo')
        fechaArticulo = request.POST.get('fechaArticulo')
        temaSeleccionado = request.POST.get('temaSeleccionado')
        temaObj = tema.objects.get(id=temaSeleccionado)
        articulo.objects.create(
            tituloArticulo = tituloArticulo,
            descripcionArticulo = descripcionArticulo,
            fechaArticulo = fechaArticulo,
            temaR=temaObj            
        )  
        return HttpResponseRedirect(reverse('wikiApp:articulos'))    
    return render(request,'nuevoArticulo.html',{
        'temasSistema':tema.objects.all()
    })    

def nuevoTema(request):
    if request.method == 'POST':
        nombreTema = request.POST.get('nombreTema')
        descripcionTema = request.POST.get('descripcionTema')
        tema.objects.create(
            nombreTema = nombreTema,
            descripcionTema = descripcionTema          
        ) 
        return HttpResponseRedirect(reverse('wikiApp:temas'))
    return render(request,'nuevoTema.html',{
        'temasSistema':tema.objects.all()
    })

def articulos(request):
    articulosTotales = articulo.objects.all()
    return render(request,'articulos.html',{
        'articulosTotales':articulosTotales,
        'temasSistema':tema.objects.all()       
    })

def temas(request):
    temasTotales = tema.objects.all()
    return render(request,'temas.html',{
        'temasTotales':temasTotales,
        'temasSistema':tema.objects.all()       
    })

def verTema(request,idTema):
    temaInfo = tema.objects.get(id=idTema)
    listaArticulos = temaInfo.articulo_set.all()
    return render(request,'verTema.html',{
        'objTema':temaInfo,
        'temasSistema':tema.objects.all(),
        'listaArticulos': listaArticulos
    })
