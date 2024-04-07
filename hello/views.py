
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import FarmingEquipment, CartItem
from django.http import JsonResponse
from decimal import Decimal

def home(request):
    return render(request, "hello/home.html")

def about(request):
    return render(request, "hello/about.html")

def contact(request):
    return render(request, "hello/contact.html")

def catalog(request):
   # Retrieve first 5 products
    products = FarmingEquipment.objects.all()[:5]

    context = {
        'products': products,
    }
    return render(request, 'hello/catalog.html', context)

def catalog1(request):
  # Retrieve the remaining products (excluding the first 5)
    remaining_products = FarmingEquipment.objects.all()[5:10]

    context = {
        'remaining_products': remaining_products,
    }
    return render(request, 'hello/catalog1.html', context)

from django.shortcuts import render, get_object_or_404

def prodDetails(request, product_name):
    product = get_object_or_404(FarmingEquipment, name=product_name)
    context = {'product': product}  # Use singular 'product' in context
    return render(request, "hello/prodDetails.html", context)

def search(request):
  search_term = request.GET.get('search', '')  # Get search term (default empty string)

  if search_term:
    products = FarmingEquipment.objects.filter(name__icontains=search_term)  # Case-insensitive search
  else:
    products = FarmingEquipment.objects.all()  # Display all products if no search term

  context = {
      'products': products,
      'search_term': search_term,  # Pass search term for potential UI updates
  }
  return render(request, "hello/search.html", context)

def add_to_cart(request, product_id):
    product = get_object_or_404(FarmingEquipment, id=product_id)

    # Use session for cart storage (example)
    cart = request.session.get('cart', [])
    existing_item = next((item for item in cart if item['id'] == str(product.id)), None)
    if existing_item:
        existing_item['quantity'] += 1
    else:
        cart.append({
            'id': str(product.id),
            'name': product.name,
            'price': str(product.price),
            'quantity': 1,
        })
    request.session['cart'] = cart

    return redirect('cart_summary')  # Redirect to cart summary page

def cart_summary(request):
    """
    Renders the cart summary page displaying cart items and totals.
    """
    cart = request.session.get('cart', [])
    total_price = sum(Decimal(item['price']) * Decimal(item['quantity']) for item in cart)
    context = {
        'cart': cart,
        'total_price': total_price,
    }
    return render(request, 'hello/cart_summary.html', context)

def checkout(request):
    """
    Checkout view to process the order and empty the cart.
    """
    # Process the order (e.g., save to database, send confirmation emails, etc.)
    # Here you can perform any necessary actions related to completing the order

    # After processing the order, empty the cart
    request.session['cart'] = []

    # Redirect the user to a thank you page or any other appropriate page
    return render(request, 'hello/checkout_thankyou.html')

def empty_cart(request):
    """
    Empty the cart by removing all items from the session.
    """
    # Remove all items from the cart session
    del request.session['cart']

    # Redirect the user back to the cart summary page or any other appropriate page
    return redirect('cart_summary')