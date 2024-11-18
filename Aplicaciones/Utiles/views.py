from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def inicioUtiles(request):
    areaSuministros = request.user.groups.filter(
        name="areaDeSuministros").exists()
    otrasAreas = request.user.groups.filter(name="otrasAreas").exists()
    return render(request, "InicioUtiles.html", {
        "esAreaDeSuministro": areaSuministros,
        "esOtrasAreas": otrasAreas,
    })
