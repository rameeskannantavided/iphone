from django.contrib import admin
from django.urls import path, include
from . import views
app_name='iphoneapp'

urlpatterns = [
    path('',views.home,name='home'),
    path('movie/<int:id>',views.details,name='details'),
    path('add/',views.add_iphone,name='add_iphone'),
    path('cart/<int:id>',views.cart,name='cart')


]
