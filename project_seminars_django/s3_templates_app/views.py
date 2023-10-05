import random

from django.shortcuts import render, redirect

from django.http import HttpResponse
import logging

from .forms import ChooseGameForm

# Create your views here.
# Задание №1
# Изменяем задачу 8 из семинара 1 с выводом двух html страниц: главной и о себе.
# Перенесите вёрстку в шаблоны.
# Представления должны пробрасывать полезную информацию в шаблон через контекст.
# Задание №2
# Доработаем задачу 1.
# Выделите общий код шаблонов и создайте родительский шаблон base.html.
# Внесите правки в дочерние шаблоны.


logger = logging.getLogger(__name__)


def main_page(request):
    context = {'explaining': 'Main page',
               'text': 'This is our welcome page, so welcome!!'}
    logger.info('Main page visited')
    return render(request, 's3_templates_app/s3_task_1_welcome.html', context=context)


def about_page(request):
    context = {'explaining': 'About me',
               'text1': 'I am supposed to tell a few words about myself on this page.',
               'text2': 'So, I live in Russia and I am learning to become a programmer. Hope I will be able to.',
               'text3': 'Also I am learning to play table tennis. This is a wonderful sport and I really hope to succeed.'}
    logger.info('About page visited')
    return render(request, 's3_templates_app/s3_task_1_about.html', context=context)


# Задание №3
# Доработаем задачу 7 из урока 1, где бросали монетку, игральную кость и генерировали случайное число.
# Маршруты могут принимать целое число - количество бросков.
# Представления создают список с результатами бросков и передают его в контекст шаблона.
# Необходимо создать универсальный шаблон для вывода результатов любого из трёх представлений.

def one(request, n: int):
    logger.info('One page started')
    context = {"explaining": "dropping coin",
               "results_head": f'Results of {n} drops: ',
               "results": {"Орел": 0, "Решка": 0}}
    for _ in range(n):
        answer = random.choice(['Орел', 'Решка'])
        if answer == 'Орел':
            context['results']['Орел'] += 1
        elif answer == 'Решка':
            context['results']['Решка'] += 1
    return render(request, 's3_templates_app/s3_t3_result.html', context=context)


def two(request, n: int):
    logger.info('Two page started')
    context = {"explaining": "dropping cube",
               "results_head": f'Results of {n} drops of cube: ',
               "results": {"1: ": 0, "2: ": 0, "3: ": 0, "4: ": 0, "5: ": 0, "6: ": 0, }}
    for _ in range(n):
        answer = f'{random.randint(1, 6)}: '
        context['results'][answer] += 1
    return render(request, 's3_templates_app/s3_t3_result.html', context=context)


def three(request, n: int):
    logger.info('Three page started')
    context = {"explaining": "random numbers",
               "results_head": f'Results of {n} random numbers: ',
               "results": {"Random_results: ": []}}
    for _ in range(n):
        answer = random.randint(0, 100)
        context['results']['Random_results: '].append(answer)
    context['results']['Random_results: '].sort()
    return render(request, 's3_templates_app/s3_t3_result.html', context=context)

# Семинар 4 Задание №2
# Доработаем задачу 1.
# Создайте представление, которое выводит форму выбора.
# В зависимости от переданных значений представление вызывает одно из трёх представлений, созданных на
# прошлом семинаре (если данные прошли проверку, конечно же).

def choose_game(request):
    if request.method == 'POST':
        form = ChooseGameForm(request.POST)
        if form.is_valid():
            game = form.cleaned_data['game']
            n = form.cleaned_data['number']
            if game == 'Drop_coin':
                return redirect(f'/s3/one/{n}')
            if game == 'Drop_cube':
                return redirect(f'/s3/two/{n}')
            if game == 'Random_number':
                return redirect(f'/s3/three/{n}')
    else:
        form = ChooseGameForm()
        return render(request, 's3_templates_app/s4_choose_game.html', {'form':form})