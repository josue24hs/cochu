from django.http import HttpResponse
from django.views.decorators.http import require_GET

@require_GET
def hola_mundo(request):
    return HttpResponse("Hola Mundo desde Django!")
