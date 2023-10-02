from django.urls import path
from . import views

urlpatterns = [
    path('', views.hw2_main, name='main_hw_2_shop'),
    path('orders_of/', views.show_order_by_client, name='see orders of client'),
    path('orders_of/<str:name>/<int:days>', views.show_ordered_by_client_timesort, name='see ordered of client'),
    path('contacts_of/', views.show_contacts_of_client, name='see contacts of client'),
]