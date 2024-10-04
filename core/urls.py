from django.urls import path

from core.views import hello_world_view

urlpatterns = [
    path("", hello_world_view),
]
