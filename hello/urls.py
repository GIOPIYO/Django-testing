from django.urls import path
from hello import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/",views.about, name="about"),
    path("contact/",views.contact, name="contact"),
    path("catalog/",views.catalog, name="catalog"),
    path("catalog1/",views.catalog1, name="catalog1"),
    path("search/", views.search, name="search"),
    path("product/<str:product_name>/", views.prodDetails, name="prodDetails"),
    path("add_to_cart/<int:product_id>/", views.add_to_cart, name="add_to_cart"),
    path("cart_summary/", views.cart_summary, name="cart_summary"),
    path('checkout/', views.checkout, name='checkout'),
    path('empty_cart/', views.empty_cart, name='empty_cart'),
]
