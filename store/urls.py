from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/', views.product_list, name='product_list'),  # Map the URL to the product_list view
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    
    
]
