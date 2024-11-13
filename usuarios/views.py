from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario
from .forms import UsuarioForm


def home(request):
    return render(request, 'index.html')

def ingresar(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ingresar')
    else:
        form = UsuarioForm()
    return render(request, 'usuarios/ingresar.html', {'form': form})

def lista(request):
    usuarios = Usuario.objects.all()
    return render(request, 'lista.html', {'usuarios': usuarios})

def eliminar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    usuario.delete()
    return redirect('lista')

def editar_usuario(request, id):
    usuario = get_object_or_404(Usuario, pk=id)  # Obtener el usuario a editar

    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)  # Cargar los datos actuales en el formulario
        if form.is_valid():
            form.save()  # Guardar los datos actualizados en la base de datos
            return redirect('lista')  # Redirigir a la lista de usuarios después de guardar
    else:
        form = UsuarioForm(instance=usuario)  # Cargar los datos actuales en el formulario si no es POST

    return render(request, 'usuarios/editar_usuario.html', {'form': form, 'usuario': usuario})
