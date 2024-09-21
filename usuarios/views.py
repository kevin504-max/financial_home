from django.shortcuts import render, get_object_or_404, redirect
from .models import Usuario
from .forms import UsuarioForm

# Create
def usuario_create(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuarios')  
    else:
        form = UsuarioForm()
    return render(request, 'usuarios/usuario_form.html', {'form': form})

# Read (List)
def usuario_list(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/usuarios.html', {'usuarios': usuarios})

# Update
def usuario_update(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('usuarios')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'usuarios/usuario_form.html', {'form': form})

# Delete
def usuario_delete(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('usuarios')
    return render(request, 'usuarios/usuario_delete.html', {'usuario': usuario})
