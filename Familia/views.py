from django.shortcuts import render
from .models import *
from django.http import *
# Create your views here.

def tios(request):

    tios=Tios(nombre="Jorge", apellido="Lopez", proveniente="papa", edad=55, nacimiento="1956-11-28")
    tios.save()
    edad2= str(tios.edad)
    nacimiento2= str(tios.nacimiento)
    cadena_Texto=str("Pariente Guardado: "+tios.nombre+" "+tios.apellido+", Proveniente de: "+tios.proveniente+", con Edad de: "+edad2+", con Fecha de Nacimiento de: "+nacimiento2)
    return HttpResponse(cadena_Texto)

def herm(request):

    herm=Hermanos(nombre="Joanna", apellido="Lopez", edad=40, nacimiento="1982-02-27")
    herm.save()
    edad2= str(herm.edad)
    nacimiento2= str(herm.nacimiento)
    cadena_Texto=str("Pariente Guardado: "+herm.nombre+" "+herm.apellido+", con Edad de: "+edad2+", con Fecha de Nacimiento de: "+nacimiento2)
    return HttpResponse(cadena_Texto)

def prim(request):

    prim=Primos(nombre="Diana", apellido="Navarrete", edad=38, nacimiento="1983-11-19")
    prim.save()
    edad2= str(prim.edad)
    nacimiento2= str(prim.nacimiento)
    cadena_Texto=str("Pariente Guardado: "+prim.nombre+" "+prim.apellido+", con Edad de: "+edad2+", con Fecha de Nacimiento de: "+nacimiento2)
    return HttpResponse(cadena_Texto)

def viven(request):

    viven=Viven(ciudad="Ticul", estado="Yucatán")
    viven.save()
    cadena_Texto=str("Pariente Vive en: "+viven.ciudad+", del Estado de: "+viven.estado)
    return HttpResponse(cadena_Texto)

def trab(request):

    trab=Trabajo(profesion="Administrador", titulo="Ingeniero", mail="admin@gmail.com", activo=1)
    trab.save()
    mail2=str(trab.mail)
    activo2=str(trab.activo)
    cadena_Texto=str("Pariente con Profesión de: "+trab.profesion+", con Título de: "+trab.titulo+"; el mail es: "+mail2+" y está en estatus: "+activo2)
    return HttpResponse(cadena_Texto)

def inicio(request):
    return render(request, 'Familia/inicio.html')

def Familia_tios(request):
    tios=Tios(nombre="Jorge", apellido="Lopez", proveniente="papa", edad=55, nacimiento="1956-11-28")
    tios.save()
    edad2= str(tios.edad)
    nacimiento2= str(tios.nacimiento)
    cadena_Texto=str("Pariente Guardado: "+tios.nombre+" "+tios.apellido+", Proveniente de: "+tios.proveniente+", con Edad de: "+edad2+", con Fecha de Nacimiento de: "+nacimiento2)
    return HttpResponse(cadena_Texto)
    #return render(request, 'Familia/Familia_tios.html')

def Familia_hermanos(request):
    herm=Hermanos(nombre="Joanna", apellido="Lopez", edad=40, nacimiento="1982-02-27")
    herm.save()
    edad2= str(herm.edad)
    nacimiento2= str(herm.nacimiento)
    cadena_Texto=str("Pariente Guardado: "+herm.nombre+" "+herm.apellido+", con Edad de: "+edad2+", con Fecha de Nacimiento de: "+nacimiento2)
    return HttpResponse(cadena_Texto)
    #return render(request, 'Familia/Familia_hermanos.html')

def Familia_primos(request):
    prim=Primos(nombre="Diana", apellido="Navarrete", edad=38, nacimiento="1983-11-19")
    prim.save()
    edad2= str(prim.edad)
    nacimiento2= str(prim.nacimiento)
    cadena_Texto=str("Pariente Guardado: "+prim.nombre+" "+prim.apellido+", con Edad de: "+edad2+", con Fecha de Nacimiento de: "+nacimiento2)
    return HttpResponse(cadena_Texto)
    #return render(request, 'Familia/Familia_primos.html')

def Familia_lugar(request):
    viven=Viven(ciudad="Ticul", estado="Yucatán")
    viven.save()
    cadena_Texto=str("Pariente Vive en: "+viven.ciudad+", del Estado de: "+viven.estado)
    return HttpResponse(cadena_Texto)
    #return render(request, 'Familia/Familia_lugar.html')

def Familia_trabajan(request):
    trab=Trabajo(profesion="Administrador", titulo="Ingeniero", mail="admin@gmail.com", activo=1)
    trab.save()
    mail2=str(trab.mail)
    activo2=str(trab.activo)
    cadena_Texto=str("Pariente con Profesión de: "+trab.profesion+", con Título de: "+trab.titulo+"; el mail es: "+mail2+" y está en estatus: "+activo2)
    return HttpResponse(cadena_Texto)
    #return render(request, 'Familia/Familia_trabajan.html')
