from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from class_date.models import conexs_pool


def bienvenida(request):
    no_conex = conexs_pool.objects.count()
    connex = conexs_pool.objects.all()
    return render(request, 'Index.html',{'no_conex': no_conex, 'connex':connex})
