from django.core.handlers.wsgi import WSGIRequest
from inertia import render


def hello_world_view(request: WSGIRequest):
    return render(request, "app.vue", props={"title": "hello world!"})
