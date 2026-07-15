from django import forms
from .models import Food

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ["food_name", "food_calories"]
        widgets = {
            "food_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Food name"
            }),
            "food_calories": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Calories"
            }),
        }