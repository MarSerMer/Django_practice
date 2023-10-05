from django import forms

# Семинар 4, Задание №1
# Доработаем задачу про броски монеты, игральной кости и случайного числа.
# Создайте форму, которая предлагает выбрать: монета, кости, числа.
# Второе поле предлагает указать количество попыток от 1 до 64.

class ChooseGameForm(forms.Form):
    game = forms.ChoiceField(choices=[('Drop_coin','Drop_coin'),
                                      ('Drop_cube','Drop_cube'),
                                      ('Random_number','Random_number')],
                             widget=forms.RadioSelect())
    number = forms.IntegerField(min_value=1,
                                max_value=64)