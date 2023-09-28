from django.shortcuts import render
from django.http import HttpResponse
import logging
from .models import Client, Product, Order

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
    client_name = request.GET.get('name')
    client = Client.objects.filter(client_name=client_name).first()
    return HttpResponse(f'Client: {client.client_name}, contact information: {client.email}, {client.phone}, {client.address}')

