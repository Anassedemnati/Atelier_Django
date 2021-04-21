from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
# def home_page(request):
#     return render(request,"home.html")

# def product(request):
#     return render(request,"products.html")
class ProductView(View):
    def get(self,request):
        products=['hp','mac','acer','dell','pak']
        return render(request,"products.html",{'products':products})

# def about(request):
#     return render(request,"about.html")
