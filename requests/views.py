from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'requests/home.html')


def asyncResponse(request):
    if request.is_ajax():
        if request.method == "POST":
            edad=request.POST.get('edad')
            print(edad)
            returnData = {
                "name": "Nacho",
                "apellido": "Serrano",
                "cargo": "Profesor adjunto",
                "edad": edad
            }
            return JsonResponse(returnData)