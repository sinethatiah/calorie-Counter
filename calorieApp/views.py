from django.shortcuts import render , redirect
from .models import *
from django.contrib import messages

# Create your views here.

def add_food(request):
    if request.method == "post":
        name = request.POST["food_name"]
        calories = request.POST["food_calories"]
        if name and calories:
            Food.objects.create(food_name=name , food_calories=calories)
            return redirect("food_list")

    all_food = Food.objects.all()
    total_calories = sum(f.calories for f in all_food)
    return render(request , food_list.html)
