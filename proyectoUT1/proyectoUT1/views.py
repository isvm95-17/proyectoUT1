from django.http import HttpResponse

def saludo_dam(request):
    return HttpResponse("¡Hola! Este es mi primer proyecto funcional con Django para el primer trabajo.")