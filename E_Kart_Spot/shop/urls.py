from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="Shop"),
    path('about/', views.about, name="AboutUs"),
    path('contact/', views.contact, name="ContactUs"),
    path('tracker/', views.tracker, name="TrakingStatus"),
    path('search/', views.search, name="Search"),
    path('products/<int:myid>', views.prodview, name="Productview"),
    path('checkout/', views.checkout, name="Checkout"),
]
