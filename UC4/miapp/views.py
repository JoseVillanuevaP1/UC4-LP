from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Course
from miapp.forms import CourseForm
from django.contrib import messages

# Create your views here.
def listar_cursos(request):
    course = Course.objects.all();
    return render(request, 'listar_cursos.html',{
        'cursos': course,
        'titulo': 'Listado de Cursos'
    })


def create_curso(request):
    if request.method == 'POST':
        formulario = CourseForm(request.POST)
        if formulario.is_valid():
            data_form = formulario.cleaned_data
            # Hay 2 formas de recuperar la información
            code = data_form.get('code')
            name = data_form['name']
            hour = data_form['hour']
            credits = data_form['credits']
            state = data_form['state']
            course = Course(
                code=code,
                name=name,
                hour=hour,
                credits=credits,
                state=state
            )
            course.save()
            
            # Crear un mensaje flash (Sesión que solo se muestra 1 vez)
            messages.success(request, f'Se agregó correctamente el curso {course.idcourse}')

            return redirect('listar_cursos')
    else:
        formulario = CourseForm()
        # Generamos un formulario vacío

    return render(request, 'create_curso.html',{
        'titulo': 'Crear Curso',
        'form': formulario
    })


def eliminar_curso(request, id):
    course = Course.objects.get(pk=id)
    course.delete()
    return redirect('listar_cursos')


def listar_carreras(request):
    return render(request, 'listar_carreras.html',{
        'titulo': 'Listado de Carreras'
    })
    

def create_carrera(request):
    return render(request, 'create_carrera.html',{
        'titulo': 'Crear Carrera'
    })