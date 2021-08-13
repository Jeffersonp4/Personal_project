from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from class_date.forms import connex_Form
from class_date.models import conexs_pool


def details_conex(request, id):
    #connex = conexs_pool.objects.get(pk=id)
    connex = get_object_or_404(conexs_pool, pk=id)
    return render(request, 'details.html', {'connex': connex})




#connex_Form = modelform_factory(conexs_pool, exclude=[])

def Add_connex(request):
    if request.method == 'POST':
        formconnex = connex_Form(request.POST)
        if formconnex.is_valid():
            formconnex.save()
            return redirect('Index')
    else:
        formconnex = connex_Form()


    return render(request, 'news.html', {'formconnex': formconnex})


