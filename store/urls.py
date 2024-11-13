from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),  # Map the URL to the product_list view
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('', views.home, name='home'),
    path('about/', views.about_us, name='about_us'),
    path('contact/', views.contact_us, name='contact_us'),
]
