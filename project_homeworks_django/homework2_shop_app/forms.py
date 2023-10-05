# - ДЗ 4:
# Создайте форму для редактирования товаров в базе данных.
#
# Измените модель продукта, добавьте поле для хранения фотографии продукта.
# Создайте форму, которая позволит сохранять фото.

from django import forms

class UpdateProductForm(forms.Form):
    product_name = forms.CharField(max_length=15,required=True)
    description = forms.CharField(widget=forms.Textarea,required=False)
    price = forms.DecimalField(min_value=0, max_value=100,required=False)
    quantity = forms.IntegerField(min_value=0,required=False)
    date_of_addition = forms.DateField(required=False)