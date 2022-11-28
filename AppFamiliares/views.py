from django.shortcuts import render
from .models import Familiares
from django.http import HttpResponse
from django.template import Template, loader

# Create your views here.


def familia(request):
    
    madre=Familiares(nombre="Marcela", edad=56, cumpleanos=("1965-6-14"))
    
    pareja=Familiares(nombre="Javier", edad=36, cumpleanos="1986-8-5")
    
    hermana=Familiares(nombre="Paula", edad=30, cumpleanos="1992-9-20")
    
    madre.save()
    hermana.save()
    pareja.save()
    
    template=loader.get_template("familiar.html")
    
    context= {"familiar": [madre,pareja,hermana]}
    
    document=template.render(context)
    return HttpResponse(document)