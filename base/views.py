from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    return render(request,"home.html")

def product(request):
    return render(request,"products.html")

def about(request):
    return render(request,"about.html")
