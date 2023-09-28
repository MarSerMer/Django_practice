from django.urls import path
from . import views

urlpatterns = [
    path('', views.seminar2, name='main_seminar_2_blog'),
    path('authors/', views.authors_read, name='authors'),
    path('articles/', views.articles_read, name='articles'),
    path('articles_by_author/', views.articles_by_author, name='articles_by_author'),

]
