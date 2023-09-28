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
    authors = Author.object.all()
    return HttpResponse(f'{authors}')


def articles_read(request):
    logger.info(f'{request} articles page visited')
    articles = Article.object.all()
    return HttpResponse(f'{articles}')


def articles_by_author(request):
    logger.info(f'{request} articles by authors page visited')
    name = request.GET.get('name')
    author_id = Author.objects.filter(first_name=name).first()
    articles = Article.objects.filter(author_id=author_id).all()
    return HttpResponse(articles)
