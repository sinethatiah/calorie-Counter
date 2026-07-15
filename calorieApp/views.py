from django.shortcuts import render , redirect
from .models import *
from django.contrib import messages
from .forms import FoodForm

# Create your views here.

from django.shortcuts import render, redirect
from .models import Food
from .forms import FoodForm

def add_food(request):
    if request.method == "POST":
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("add_food")
    else:
        form = FoodForm()

    all_food = Food.objects.all()
    total_calories = sum(f.food_calories for f in all_food)
    return render(request, "food_list.html", {
        "form": form,
        "foods": all_food,
        "total_calories": total_calories,
    })

def reset_foods(request):
    Food.objects.all().delete()
    return redirect("add_food")

        
