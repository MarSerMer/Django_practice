from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
# Создайте три модели Django: клиент, товар и заказ.
#
# Клиент может иметь несколько заказов.
# Заказ может содержать несколько товаров.
# Товар может входить в несколько заказов.
#
# Поля модели «Клиент»:
# — имя клиента
# — электронная почта клиента
# — номер телефона клиента
# — адрес клиента
# — дата регистрации клиента


class Client(models.Model):
    client_name = models.CharField(max_length=42)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=40)
    date_of_reg = models.DateField()

    def __str__(self):
        return f'Client: {self.client_name}, contacts: {self.phone}, {self.email}, {self.address}'


    def __unicode__(self):
        return self.client_name

# Поля модели «Товар»:
# — название товара
# — описание товара
# — цена товара
# — количество товара
# — дата добавления товара

# Домашнее задание 4:
# Измените модель продукта, добавьте поле для хранения фотографии продукта.
# Создайте форму, которая позволит сохранять фото.


class Product(models.Model):
    product_name = models.CharField(max_length=15)
    description = models.TextField()
    price = models.DecimalField(validators=[MinValueValidator(0), MaxValueValidator(100)],
                                decimal_places=2,
                                max_digits=10)
    quantity = models.PositiveIntegerField(default=0)
    date_of_addition = models.DateField()
    image = models.ImageField(upload_to='products_images/',blank=True, null=True)

    @staticmethod
    def information(self):
        return f'Product: {self.product_name}, {self.description}'

    def __str__(self):
        return f'Product: {self.product_name}, {self.description}, ' \
               f'price: {self.price}, available from: {self.date_of_addition}, ' \
               f'pieces left: {self.quantity}'

    def __unicode__(self):
        return self.product_name


# Поля модели «Заказ»:
# — связь с моделью «Клиент», указывает на клиента, сделавшего заказ
# — связь с моделью «Товар», указывает на товары, входящие в заказ
# — общая сумма заказа
# — дата оформления заказа


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    # поле сумма заказа при создании = 0, а потом хорошо бы вписать куда-нибудь подсчет и запись нового значения
    sum_of_order = models.DecimalField(validators=[MinValueValidator(0), MaxValueValidator(100)],
                                       decimal_places=2,
                                       max_digits=20,
                                       default=0)
    date_of_order = models.DateField()

    def __str__(self):
        return f'Order: {self.id}, ordered by: {self.client}'
