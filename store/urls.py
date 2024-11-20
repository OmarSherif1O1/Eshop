from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('product/', views.product_list, name='product_list'),  # Map the URL to the product_list view
    path('product/<int:id>/', views.product_detail, name='product_detail'),
     path('cart/', views.cart_view, name='cart'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),

    
    
    
]
