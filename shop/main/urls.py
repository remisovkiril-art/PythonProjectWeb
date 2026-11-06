from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('card/<int:id>/', views.get_card, name='get_card'),
    path('search/', views.search_card, name='search_card'),
]