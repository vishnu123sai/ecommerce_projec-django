from django.urls import path, include
from django.contrib import admin
from .views import catalog, cart, removeCart, checkout, completeOrder, adminPage, adminLoginPage, fulFilled

urlpatterns = [
    path('', catalog, name="catalog"),
    path('cart/'  , cart, name="cart"),
    path('cart/remove/', removeCart, name="removecart"),
    path('cart/checkout/', checkout, name="checkout"),
    path('cart/checkout/complete', completeOrder, name="complete"),
    path('admin_page/', adminLoginPage  , name='admin_page'),
    path('admin_loggedin', adminPage, name="admin"),
    path('admin_loggedin/fulfilled/',fulFilled, name="fulfilled"),
]