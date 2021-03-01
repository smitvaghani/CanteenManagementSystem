from django.urls import path
from login import views
urlpatterns = [
    path('', views.login),
    path('register/', views.register),
    path('logout/',views.logout_view)
]
