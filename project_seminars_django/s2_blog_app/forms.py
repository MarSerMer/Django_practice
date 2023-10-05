# Семинар 4 Задание №3
# Продолжаем работу с авторами, статьями и комментариями.
# Создайте форму для добавления нового автора в базу
# данных.
# Используйте ранее созданную модель Author
from typing import Tuple, Any

from django import forms
from django.forms import models

from .models import Author, Article


class AddAuthorForm(forms.Form):
   first_name = forms.CharField(max_length=100)
   last_name = forms.CharField(max_length=100)
   email = forms.EmailField()
   biography = forms.CharField(widget=forms.Textarea)
   birthday = forms.DateField()

# Задание №4
# Аналогично автору создайте форму добавления новой статьи.
# Автор статьи должен выбираться из списка (все доступные в базе данных авторы).
def get_authors()-> tuple[tuple[Any, Any], ...]:
   res_list = []
   authors = Author.objects.all()
   for author in authors:
      res = (author.id, author.last_name)
      res_list.append(res)
   res_t = tuple(res_list)
   return res_t


class AddNewArticleForm(forms.Form):
   author = forms.ChoiceField(choices=get_authors())
   #author = forms.ModelChoiceField(queryset=models.Author.objects.all())
   title = forms.CharField(max_length=200)
   content = forms.CharField(widget=forms.Textarea)
   date_of_publ = forms.DateField()
   category = forms.CharField(max_length=100)
   is_published = forms.BooleanField(required=False)


# на семинаре показали и такой способ, он как-то сам таскает поля из базы:
# При этом в представлении (=во вьюшке) не надо отдельно создавать экземпляр класса Artice,
# пишем form = NewArt(request.POST), далее form.save() и всё
# class NewArt(forms.ModelForm):
#    class Meta:
#       model = models.Article
#       fields = ['title','author_id', 'content','date_of_publ']
#       labels = {'title':'','author_id':'', 'content':'','date_of_publ':''}
#       widgets = {
#          'title': forms.TextInput(attrs={'class':'input_text_long_input', 'placeholder':'Название статьи'}),
#          'author_id': forms.Select(attrs={'class':'input_text_long_input'}),
#          'content': forms.Textarea (attrs={'class':'input_text_long_input',
#                                            'cols':100, 'rows':10,
#                                            'placeholder':'Содержание статьи'}),
#          'date_of_publ':forms.DateInput(attrs={'type':'date'})
#       }
