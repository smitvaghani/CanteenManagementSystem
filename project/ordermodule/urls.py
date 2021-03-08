from django.urls import path
from ordermodule import views

urlpatterns = [
    path('order/', views.category),
    path('items/<str:cate_name>', views.sample,name="items")
]
