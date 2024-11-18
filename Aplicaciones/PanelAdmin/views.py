from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q


# Create your views here.


@login_required
def administracion(request):
    if not request.user.is_superuser:
        messages.error(
            request, "No tienes permisos para acceder a esta página.")
        return redirect('inicioUtiles')

    listaUsuarios = User.objects.all()
    # Busqueda
    busqueda = request.POST.get("buscar")
    if busqueda:
        try:
            busqueda_int = int(busqueda)
            listaUsuarios = User.objects.filter(
                Q(id=busqueda_int) |
                Q(username__icontains=busqueda) |
                Q(groups__name__icontains=busqueda)
            ).distinct()
        except ValueError:
            listaUsuarios = User.objects.filter(
                Q(username__icontains=busqueda) |
                Q(groups__name__icontains=busqueda) 

            ).distinct()

    # Paginacion
    paginator = Paginator(listaUsuarios, 4)
    pagina = request.GET.get("page") or 1
    posts = paginator.get_page(pagina)
    paginaActual = int(pagina)
    paginas = range(1, posts.paginator.num_pages + 1)

    groupMapping = {
        1: "Área de Suministros",
        2: "Otras Áreas",
    }

    return render(request, "panelAdmin.html", {
        "posts": posts,
        "groupMapping": groupMapping,
        "paginas": paginas,
        "paginaActual": paginaActual,

    })


def editarUsuario(request, id):
    usuario = User.objects.get(id=id)

    if request.method == 'POST':
        grupoId = request.POST.get('grupo')
        grupo = Group.objects.get(id=grupoId)

        usuario.groups.clear()
        usuario.groups.add(grupo)
        usuario.save()

        return redirect('administracion')

    return redirect('intranet')


def eliminarUsuario(request, id):
    usuario = User.objects.get(id=id)
    usuario.delete()
    return redirect('administracion')
