from django.shortcuts import render
import random
from django.http import HttpResponse
import logging

# Create your views here.
# Создайте новое приложение. Подключите его к проекту.
# В приложении должно быть три простых представления, возвращающих HTTP ответ:
# Орёл или решка
# Значение одной из шести граней игрального кубика
# Случайное число от 0 до 100

logger = logging.getLogger(__name__)


def one(request):
    logger.info('One page started')
    answer = ['Орел', 'Решка']
    i = random.randint(0, 1)
    return HttpResponse(f'{answer[i]}')


def two(request):
    logger.info('Two page started')
    answer = random.randint(1, 6)
    return HttpResponse(f'{answer}')


def three(request):
    logger.info('Three page started')
    answer = random.randint(0, 100)
    return HttpResponse(f'{answer}')
