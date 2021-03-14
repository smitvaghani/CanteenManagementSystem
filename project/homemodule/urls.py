from django.urls import path
from homemodule import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('about/', views.about),
    path('blog/', views.blog),
    path('index/', views.index),
    path('recipe/', views.recipe),
    path('feedback/', views.feed_back),
]

urlpatterns = urlpatterns + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
