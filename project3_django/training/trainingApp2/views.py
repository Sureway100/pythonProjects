from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def register(request):
    return render(request, "trainingApp2/register.html")

# def register(request):
#     return HttpResponse("hello world war")
