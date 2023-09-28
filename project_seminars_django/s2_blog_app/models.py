from django.db import models

# Create your models here.
# Задание №3
# Создайте модель Автор. Модель должна содержать следующие поля:
# ○ имя до 100 символов
# ○ фамилия до 100 символов
# ○ почта
# ○ биография
# ○ день рождения
# Дополнительно создай пользовательское поле “полное имя”, которое возвращает имя и фамилию.

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.TextField()
    birthday = models.DateField()

    @staticmethod
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.birthday}'


# Задание №4
# Создайте модель Статья (публикация). Авторы из прошлой задачи могут
# писать статьи. У статьи может быть только один автор. У статьи должны быть
# следующие обязательные поля:
# ○ заголовок статьи с максимальной длиной 200 символов
# ○ содержание статьи
# ○ дата публикации статьи
# ○ автор статьи с удалением связанных объектов при удалении автора
# ○ категория статьи с максимальной длиной 100 символов
# ○ количество просмотров статьи со значением по умолчанию 0
# ○ флаг, указывающий, опубликована ли статья со значением по умолчанию False

class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_of_publ = models.DateField()
    category = models.CharField(max_length=100)
    amount_of_views =models.IntegerField(default=0)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        res = ''
        if self.is_published:
            res = f'{self.title} : published {self.date_of_publ}, category: {self.category}, ' \
                  f'starts like: {self.content[0:15]}'
        else:
            res = f'{self.title} : not published yet, category: {self.category}, ' \
                  f'starts like: {self.content[0:15]}'
        return res