from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Index'),
    path('demo/', views.demo, name='Demo'),
    path('contactus/', views.contactus, name='ContactUs'),
    path('aboutus/', views.aboutus, name='AboutUs'),
    path('tracker/', views.tracker, name='Tracker'),
    path('search/', views.search, name='Search'),
    path('products/<int:myid>', views.productView, name='ProdView'),
    path('checkout/', views.checkout, name='Checkout'),
]