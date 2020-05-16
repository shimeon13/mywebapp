from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("weight_calculate_input", views.hello_get_query, name="weight_calculate_input"),
    path("weight_calculate_output", views.weight_calculate_output),
]
