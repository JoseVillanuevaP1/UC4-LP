from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def listar_cursos(request):
    return render(request, 'listar_cursos.html',{
        'titulo': 'Listado de Cursos'
    })


def create_curso(request):
    return render(request, 'create_curso.html',{
        'titulo': 'Crear Curso'
    })

def listar_carreras(request):
    return render(request, 'listar_carreras.html',{
        'titulo': 'Listado de Carreras'
    })
    

def create_carrera(request):
    return render(request, 'create_carrera.html',{
        'titulo': 'Crear Carrera'
    })