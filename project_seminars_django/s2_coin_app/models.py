from django.db import models
from django.utils import timezone


# Create your models here.
# Задание №1
# Создайте модель для запоминания бросков монеты: орёл или
# решка.
# Также запоминайте время броска
# Задание №2
# Доработаем задачу 1.
# Добавьте статический метод для статистики по n последним броскам монеты.
# Метод должен возвращать словарь с парой ключей-значений, для орла и для решки.
class HeadsTails(models.Model):
    rest_time = models.DateTimeField(default=timezone.now)
    res = models.CharField(max_length=10)

    @staticmethod
    def statistic(n):
        n = int(n)
        dict_res = {'Орёл': 0, 'Решка': 0}
        query = list(HeadsTails.objects.all())
        list_res = []
        if len(query) >= n:
            list_res = query[-n:]
        elif len(query) < n:
            list_res = query
        for item in list_res:
            if item.res == 'Орёл':
                dict_res['Орёл'] += 1
            elif item.res == 'Решка':
                dict_res['Решка'] += 1
        return f'Статистика по последним {n} броскам: орлы: {dict_res["Орёл"]}, решки: {dict_res["Решка"]}'

    def __str__(self):
        return f'The coin was dropped at {self.rest_time} and it showed {self.res}'
