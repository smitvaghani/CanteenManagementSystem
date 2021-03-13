from django.urls import path
from . import views

urlpatterns = [
    path('add_to_cart/', views.add_to_cart),
    path('show_cart/', views.show_cart),
    path('plus_cart/', views.plus_cart),
    path('minus_cart/', views.minus_cart),
    path('remove_cart/', views.remove_cart),
]
