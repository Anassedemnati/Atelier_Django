from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(),name="home"),
    path('products/', views.ProductView.as_view(),name="products"),
    
    

]