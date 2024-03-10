from django.urls import path

from creatures import views

urlpatterns = [
    path("", views.index, name="index"),
]
