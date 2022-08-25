from signal import SIG_DFL
from django.http.response import JsonResponse
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Negocios
from django.utils.decorators import method_decorator
import json

# Create your views here.


class VistaNegocios(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id=0):
        if(id>0):
            negocios=list(Negocios.objects.filter(id=id).values())
            if len(negocios) > 0:
                negocio = negocios[0]
                datos={'message':"Success",'negocios':negocio}
            else:
                datos={'message':"No se encontraron negocios"}
            return JsonResponse(datos)
        else:
            negocios = list(Negocios.objects.values())
            if len(negocios)>0:
                datos={'message':"Success",'negocios':negocios}
            else:
                datos={'message:': "No se encontraron negocios"}
            return JsonResponse(datos)
            
    
    def post(self, request):
        jd = json.loads(request.body)
        Negocios.objects.create(name=jd['name'], website = jd['website'], foundation = jd['foundation'] )
        datos={'message':"Success"}
        return JsonResponse(datos)
    
    def put(self, request, id):
        jd = json.loads(request.body)
        negocios=list(Negocios.objects.filter(id=id).values())
        if len(negocios) > 0:
            negocio=Negocios.objects.get(id=id)
            negocio.name = jd['name']
            negocio.website = jd['website']
            negocio.foundation = jd['foundation']
            negocio.save()
            datos={'message':"Success"}
        else:
            datos={'message:': "No se encontraron negocios"}
        return JsonResponse(datos)
                
    def delete(self, request, id):
        negocios=list(Negocios.objects.filter(id=id).values())
        if len(negocios) > 0:
            Negocios.objects.filter(id=id).delete()
            datos={'message':"Success"}
        else:
            datos={'message:': "No se encontraron negocios"}
        return JsonResponse(datos)
    
    
class Usuarios(View):
      
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        usuarios=list(User.objects.values())
        usuario = usuarios[0]
        datos={'message':"Sucess",'usuarios':usuarios}
        return JsonResponse(datos)
    
    def post(self, request):
        jd = json.loads(request.body)
        usuarios=list(User.objects.values())
        usuario = usuarios[0]
        datos={'message':"Sucess",'usuarios':jd}
        return JsonResponse(datos)