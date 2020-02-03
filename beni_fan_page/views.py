# bani_fan_page/views.py

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello world! Welcome to Beni's Fan Page")
