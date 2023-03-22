from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# def welcome(request, name):
#     return HttpResponse(f"Hello, Welcome {name}")

def welcome(request, name):
    return render(request, "trainingAppx/dashboard.html", {
        "name": name.capitalize()
    })
