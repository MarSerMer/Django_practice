from django.urls import path
from . import views

urlpatterns = [
    path('', views.hw_shop_main, name='main_hw_2_shop'),
    # OK http://127.0.0.1:8000/shop/
    path('orders_of/', views.show_order_by_client, name='see orders of client'),
    # OK http://127.0.0.1:8000/shop/orders_of/?name=Name1
    path('orders_of/<str:name>/<int:days>/', views.show_ordered_by_client_timesort, name='see ordered by client'),
    # OK http://127.0.0.1:8000/shop/orders_of/Name12/500/
    path('contacts_of/', views.show_contacts_of_client, name='see contacts of client'),
    # OK http://127.0.0.1:8000/shop/contacts_of/?name=Name1
    path('upf/<int:pr_id>/', views.update_product_form, name='update product'),
    # OK http://127.0.0.1:8000/shop/upf/2
    path('img/<int:pr_id>/', views.upload_product_image_form, name='upload image'),
]