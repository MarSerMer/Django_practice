from django.contrib import admin
from .models import Author, Article


# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'birthday']

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_of_publ', 'author', 'category']
    ordering = ['-category', '-date_of_publ']
    fields = ['author', 'title', 'content', 'date_of_publ', 'category', 'amount_of_views', 'is_published']
    readonly_fields = ['amount_of_views']

admin.site.register(Author, AuthorAdmin)
admin.site.register(Article, ArticleAdmin)
