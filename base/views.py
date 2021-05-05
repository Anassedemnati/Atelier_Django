from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.

class ProductView(View):
    def get(self,request):
        products=['hp','mac','acer','dell','pak']
        return render(request,"products.html",{'products':products})



class IndexView(View):
    def get(self,request):
        return render(request,"index.html",{})