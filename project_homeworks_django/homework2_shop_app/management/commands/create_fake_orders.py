from django.core.management.base import BaseCommand
import random
from datetime import datetime as DT
from datetime import timedelta
from homework2_shop_app.models import Client, Product, Order

START = DT.strptime('01.01.2023', '%d.%m.%Y')
END = DT.strptime('29.09.2023', '%d.%m.%Y')


def get_random_date(start=START, end=END):
    delta = end - start
    return start + timedelta(random.randint(0, delta.days))


class Command(BaseCommand):
    help = 'Creates fake orders'

    def add_arguments(self, parser):
        parser.add_argument('number', type=int, help='how many orders needed')

    def handle(self, *args, **kwargs):
        number = kwargs['number']
        list_of_clients = Client.objects.all()
        list_of_products = Product.objects.all()
        for i in range(1, number + 1):
            order_client = random.choice(list_of_clients)
            n = random.randint(1, 5)
            prods_to_order = []
            i = 0
            while i < n:
                prod = random.choice(list_of_products)
                if prod not in prods_to_order:
                    prods_to_order.append(prod)
                    i += 1
                else:
                    continue
            order = Order(client=order_client,
                          # products=prods_to_order[0],
                          date_of_order = get_random_date())
            order.save()
            for i in range(len(prods_to_order)):
                order.products.add(prods_to_order[i])
                order.save()
        return f'{number} fake orders created'
