from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse


def hello_world_view(request: WSGIRequest):
    return HttpResponse("hello world!")
