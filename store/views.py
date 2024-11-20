from django.shortcuts import render, get_object_or_404
from .models import Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages  # For error messages
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem
from django.db.models import F, Sum




def registration_page(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'accounts/register.html' , context)

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # Get username from form
        password = request.POST.get('password')  # Get password from form
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Log the user in
            login(request, user)
            return redirect('home')  # Redirect to homepage or desired page
        else:
            # Display an error message
            messages.error(request, 'Invalid username or password')
    context = {}
    return render(request, 'accounts/login.html' , context) 
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login after logout



def product_list(request):
    products = Product.objects.all()  # Fetch all products from the database
    return render(request, 'product/product_list.html', {'products': products})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product/product_detail.html', {'product': product})

def home(request):
    return render(request, 'store/home.html')

def about_us(request):
    return render(request, 'store/about_us.html')

def contact_us(request):
    return render(request, 'store/contact_us.html')

@login_required
def cart_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    total = 0
    for item in cart.items.all() :
        total+=item.get_total_price()
       
    
    return render(request, 'store/cart.html', {'cart': cart, 'total': total})


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)

    # Check if the item already exists in the cart
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not item_created:
        cart_item.quantity += 1  # Increment quantity if already in cart
    cart_item.save()
    return redirect('cart')  # Redirect to cart page

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    cart_item.delete()
    return redirect('cart')  # Redirect to cart page