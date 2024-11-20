from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.description}"

class Product(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    has_colors = models.BooleanField(default=False)  # Enable/disable color feature
    colors = models.TextField(blank=True, null=True, help_text="Comma-separated list of colors")

    def get_color_list(self):
        """Return a list of colors from the comma-separated string."""
        if self.colors:
            return [color.strip() for color in self.colors.split(',')]
        return []

    def __str__(self):
        return self.name
    
    from django.contrib.auth.models import User
from store.models import Product  # Assuming your product model is in store.models

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"

    def get_total_price(self):
        return self.product.price * self.quantity
