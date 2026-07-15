from django.urls import path
from . import views

urlpatterns = [
    path("", views.add_food, name="add_food"),
    path("reset/", views.reset_foods, name="reset_foods"),
]