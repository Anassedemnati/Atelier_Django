from django.urls import path,include
from . import views
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = [
    path('', views.IndexView.as_view(),name="home"),
    path('products/', views.ProductlistView.as_view(),name="productslist"),
    path('products/create', views.ProductView.as_view(),name="productcreate"),
    path('categoies/create', views.CategoryView.as_view(),name="CategoryCreate"),
    path('categoies/', views.CategorylistView.as_view(),name="Categorylist"),
    
    

]