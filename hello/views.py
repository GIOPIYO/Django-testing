
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render
from .models import FarmingEquipment

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

def prodDetails(request, product_name):
    try:
        product = FarmingEquipment.objects.get(name=product_name)
    except FarmingEquipment.DoesNotExist:
        # Handle product not found case (optional)
        return render(request, 'product_not_found.html')  # Example error template

    context = {
        'products': product,
    }
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