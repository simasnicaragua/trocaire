from django.shortcuts import render_to_response
from django.template.context import RequestContext
from trocaire.encuesta.views import consultar
from trocaire.mujeres_hombres.views import *

def consultarpf(request):
    request.session['centinela'] = 0
    return consultar(request, pf=1)

def proposito(request):
    return render_to_response('pf/proposito.html', RequestContext(request, locals()))

def fin(request):
    return render_to_response('pf/fin.html', RequestContext(request, locals()))