from django.urls import path
from ordermodule import views

urlpatterns = [
    path('category/', views.category),
    path('items/<str:cate_name>', views.items, name="items"),
    path('search/', views.searchItem)
]
