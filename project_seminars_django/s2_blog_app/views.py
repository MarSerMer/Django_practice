from django.shortcuts import render
import random
from django.http import HttpResponse
import logging

from django.utils import timezone

from .models import Author, Article

# Create your views here.

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO, filename='logs/seminar2-blog.log', filemode='a')


def seminar2(request):
    logger.info(f'{request} request received')
    return HttpResponse("Seminar 2 page - blog task")


def authors_read(request):
    logger.info(f'{request} authors page visited')
    authors = Author.objects.all()
    return HttpResponse(authors)


def articles_read(request):
    logger.info(f'{request} articles page visited')
    articles = Article.objects.all()
    return HttpResponse(articles)


def articles_by_author(request):
    logger.info(f'{request} articles by authors page visited')
    name = request.GET.get('name')
    author_id = Author.objects.filter(first_name=name).first()
    articles = Article.objects.filter(author_id=author_id).all()
    return HttpResponse(articles)


# Семинар 3, Задание №4
# Доработаем задачи из прошлого семинара по созданию моделей автора, статьи и комментария.
# Создайте шаблон для вывода всех статей автора в виде списка заголовков.
# ○ Если статья опубликована, заголовок должен быть ссылкой на статью.
# ○ Если не опубликована, без ссылки.
# Не забываем про код представления с запросом к базе данных и маршруты.

def articles_by_author_template(request):
    logger.info(f'{request} articles by authors template page visited')
    name = request.GET.get('name')
    author_id = Author.objects.filter(first_name=name).first()
    articles = Article.objects.filter(author_id=author_id).all()
    context = {'author': name, 'articles': articles}
    return render(request, 's2_blog_app/articles_by_author.html', context=context)


def show_article(request, art_id):
    logger.info(f'Show article page visited')
    article = Article.objects.get(id=art_id)
    article.amount_of_views += 1
    article.save()
    context = {'article': article}
    return render(request, 's2_blog_app/show_article.html', context=context)
