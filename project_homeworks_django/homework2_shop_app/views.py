from django.shortcuts import render
from django.http import HttpResponse
import logging
from datetime import datetime
from datetime import timedelta
from .models import Client, Product, Order
from .forms import UpdateProductForm

# Create your views here.

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO, filename='logs/homework2-shop.log', filemode='a')


def hw2_main(request):
    return HttpResponse('Homework 2 -shop- main page')


def show_order_by_client(request):
    name = request.GET.get('name')
    client_id = Client.objects.filter(client_name=name).first()
    orders = Order.objects.filter(client_id=client_id).all()
    return HttpResponse(orders)


def show_contacts_of_client(request):
    print('show_contacts_of_client started')
    client_name = request.GET.get('name')
    client = Client.objects.filter(client_name=client_name).first()
    return HttpResponse(
        f'Client: {client.client_name}, contact information: {client.email}, {client.phone}, {client.address}')


# Домашнее задание 3:
# Продолжаем работать с товарами и заказами.
# Создайте шаблон, который выводит список заказанных клиентом товаров из всех его заказов с сортировкой по времени:
# — за последние 7 дней (неделю)
# — за последние 30 дней (месяц)
# — за последние 365 дней (год)
# Товары в списке не должны повторятся.

def show_ordered_by_client_timesort(request, name, days):
    print('show_ordered_by_client_timesort started')
    client_id = Client.objects.filter(client_name=name).first()
    orders = Order.objects.filter(client_id=client_id).all()
    res_set = set()
    for ord in orders:
        print(ord.date_of_order + timedelta(days))
        if ord.date_of_order + timedelta(days) >= datetime.now().date():
            prods = ord.products.all()
            for pr in prods:
                res_set.add(pr.product_name)
    context = {'days': days,
               'ordered': res_set,
               'name': name}
    return render(request, 'homework2_shop_app/show_orders_of_client_timesort.html', context=context)

# Домашнее задание 4:
# Создайте форму для редактирования товаров в базе данных.

def update_product_form(request,name):
    if request.method == 'POST':
        form = UpdateProductForm(request.POST)
        if form.is_valid():
            product_name = form.cleaned_data['product_name']
            product = Product.objects.filter(product_name=name).first()
            description = form.cleaned_data['product_name']
            price = form.cleaned_data['product_name']
            quantity = form.cleaned_data['product_name']
            date_of_addition = form.cleaned_data['product_name']
            if description:
                product.description = description
            if price:
                product.price = price
            if quantity:
                product.quantity = quantity
            if date_of_addition:
                product.date_of_addition = date_of_addition
            product.save()
            return HttpResponse('<h2>Product updated.</h2>')
    else:
        # pr_name = request.GET.get('pr_name')
        product = Product.objects.filter(product_name=name).first()
        if product:
            form = UpdateProductForm()
            message = 'Enter information to update product. Be careful about product name!'
            return render(request, 'homework2_shop_app/update_product_form.html', {'form': form, 'message': message})
        else:
            return HttpResponse('<h2>Such product was not found.</h2>')

def wtf_2(request):
    return HttpResponse("wtf??")