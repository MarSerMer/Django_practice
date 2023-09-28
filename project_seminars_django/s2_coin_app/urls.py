from django.urls import path
from . import views

urlpatterns = [
    path('', views.seminar2, name='main_seminar_2_coins'),
    path('coins/', views.heads_tails, name='coin_seminar_2'),
]
