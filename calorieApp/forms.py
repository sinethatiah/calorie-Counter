from django import forms
from .models import Food

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ["name", "calories"]
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Food name"
            }),
            "calories": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Calories"
            }),
        }