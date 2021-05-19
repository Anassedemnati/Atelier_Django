from django import forms
from django.db.models.base import Model
from .models import *
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields ="__all__"