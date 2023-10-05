from django.shortcuts import render
from django.http import HttpResponse
import logging

from .models import Author, Article
from .forms import AddAuthorForm, AddNewArticleForm
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

# Семинар 4 Задание №3
# Продолжаем работу с авторами, статьями и комментариями.
# Создайте форму для добавления нового автора в базу данных.
# Используйте ранее созданную модель Author

def add_author_form(request):
    message = ''
    if request.method == 'POST':
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            biography = form.cleaned_data['biography']
            birthday = form.cleaned_data['birthday']
            author = Author(first_name=first_name,
                            last_name=last_name,
                            email=email,
                            biography=biography,
                            birthday=birthday)
            author.save()
            return HttpResponse('<h2>New author saved.</h2>')
    else:
        form = AddAuthorForm()
        message = 'Enter information to create a new author.'
        return render(request, 's2_blog_app/add_author_form.html', {'form':form, 'message':message})

# Семинар 4 Задание №3
# Задание №4
# Аналогично автору создайте форму добавления новой статьи.
# Автор статьи должен выбираться из списка (все доступные в базе данных авторы).

def add_new_article_form(request):
    if request.method == 'POST':
        form = AddNewArticleForm(request.POST)
        if form.is_valid():
            author_id = form.cleaned_data['author']
            author = Author.objects.filter(id=author_id).first()
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            date_of_publ = form.cleaned_data['date_of_publ']
            category = form.cleaned_data['category']
            is_published = form.cleaned_data['is_published']
            article = Article(author=author,
                            title=title,
                            content=content,
                            date_of_publ=date_of_publ,
                            category=category,
                            is_published=is_published)
            article.save()
            return HttpResponse('<h2>New article saved.</h2>')
    else:
        form = AddNewArticleForm
        message = 'Enter information to create a new article.'
        return render(request, 's2_blog_app/add_article_form.html', {'form':form, 'message':message})