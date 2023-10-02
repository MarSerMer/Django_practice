from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_seminar_3'),
    path('about/', views.about_page, name='about_seminar_3'),
    path('one/<int:n>', views.one, name='drop_coin'),
    path('two/<int:n>', views.two, name='drop_cube'),
    path('three/<int:n>', views.three, name='random_number'),
]
