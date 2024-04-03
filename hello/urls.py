from django.urls import path
from hello import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/",views.about, name="about"),
    path("contact/",views.contact, name="contact"),
    path("catalog/",views.catalog, name="catalog"),
    path("catalog1/",views.catalog1, name="catalog1"),
    path("prodDetails/", views.prodDetails, name="prodDetails"),
    path("search/", views.search, name="search"),
]
