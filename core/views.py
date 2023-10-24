from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Entidad, Comunicado
# Create your views here.

def index(request):
        Comunicados = Comunicado.objects.all().order_by('-fecha_publicacion')
        filtro = request.POST.get('Filtrar')
        if filtro:
                Comunicados = Comunicados.filter(entidad=filtro)
        datos = {
        "Comunicados":Comunicados,
        "Entidades":Entidad.objects.all()
        }
        return render(request, 'core/index.html', datos)
    