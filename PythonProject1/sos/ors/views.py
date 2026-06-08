from django.http import HttpResponse
from django.shortcuts import render


def test_sos(request):
    return HttpResponse("<h1>welcome to sos app </h1>")

def welcome(request):
    return render(request, "welcome.html")
def signin (request):
    return render(request, "registrations.html")
def signup(request):
    return render(request, "login.html")
def header(request):
    return render(request, "header.html")

