from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('products/', views.products,name="products"),
    path('customers/<str:pk_test>/',views.customers,name="customers"),
    path('createOrder/',views.createOrder,name="createOrder"),
    path('updateOrder/<str:pk>/',views.updateOrder,name="updateOrder"),
    path('delete/<str:pk>/',views.delete, name="delete"),

]
