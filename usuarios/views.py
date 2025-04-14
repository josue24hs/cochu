from django.http import HttpResponse

def hola_mundo(request):  # Asegúrate de que se reciba `request` como argumento
    return HttpResponse("Hola Mundo desde Django!")
