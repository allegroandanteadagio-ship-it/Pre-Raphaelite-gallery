
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('artists/', views.artist_list, name='artist_list'),  # ← artist_list (единственное число!)
    path('artworks/', views.artwork_list, name='artwork_list'),  # ← artwork_list (единственное число!)
]