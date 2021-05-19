from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import *
from .form import *


# Create your views here.
class ProductlistView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, "product_list.html", {'products': products})


class CategorylistView(View):
    def get(self, request):
        Categorys = Category.objects.all()
        return render(request, "category_list.html", {'Categorys': Categorys})


def post(request):
    form = ProductForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
    return redirect("productslist")


class ProductView(View):
    def get(self, request):
        form = ProductForm()

        return render(request, "product_form.html", {'form': form})


class CategoryView(View):
    def get(self, request):
        form = CategoryForm()
        return render(request, "category_form.html", {'form': form})

    def post(self, request):
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect("Categorylist")


class IndexView(View):
    def get(self, request):
        return render(request, "index.html", {})
