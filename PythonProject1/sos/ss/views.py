from django.http import HttpResponse


def test_ss(request):
    return HttpResponse("<h1>welcome to ss app </h1>")
