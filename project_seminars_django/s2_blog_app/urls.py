from django.urls import path
from . import views

urlpatterns = [
    path('', views.seminar2, name='main_seminar_2_blog'),
    path('authors/', views.authors_read, name='authors'),
    path('articles/', views.articles_read, name='articles'),
    path('articles_by_author/', views.articles_by_author_template, name='articles_by_author'),
    path('show_article/<int:art_id>', views.show_article, name='show_article'),
    path('add_author_form/', views.add_author_form, name='add_author_form'),
    path('add_article_form/', views.add_new_article_form, name='add_article_form'),
]
