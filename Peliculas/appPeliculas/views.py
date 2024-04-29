from django.shortcuts import render;
from django.db import Error;
from appPeliculas.models import genero, peliculas;
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt

# Create your views here.

def inicio (request):
    return render (request, "1Vista.html");

def vistaAgregargenero(request):
    return render (request, "agregarGenero.html");

@csrf_exempt
def agregarGenero (request):
    try :
        nombre = request.POST['nombre'];
        #Crear objeto de tipo genero
        gener = genero(gen_nombre=nombre);
        #Salvar el genero y guardarlo en la base de datos
        gener.save();
        mensaje = "Genero agrgado exitosamente";
    except Error as error :
        mensaje = str(error);
    
    retorno = {"mensaje":mensaje};
    # return JsonResponse(retorno);
    return render(request, "agregargenero.html", retorno);

def listarPeliculas (request):
    movies = peliculas.objects.all();
    
    retorno = {"movies" : movies}
    
    # return JsonResponse(retorno);
    return render (request, "listarPeliculas.html", retorno)