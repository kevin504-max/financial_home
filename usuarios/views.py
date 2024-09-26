from django.shortcuts import render, get_object_or_404, redirect
from .models import Usuario
from .forms import UsuarioForm
from django.core.paginator import Paginator

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
    usuarios = Usuario.objects.all().order_by('nome')
    paginator = Paginator(usuarios, 6)  
    page_number = request.GET.get('page')
    usuarios_paginated = paginator.get_page(page_number)
    return render(request, 'usuarios/usuarios.html', {'usuarios': usuarios_paginated})

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
