from _decimal import Decimal
from django.core.management.base import BaseCommand
import random
from datetime import datetime as DT
from datetime import timedelta
from homework2_shop_app.models import Product

START = DT.strptime('01.01.2022', '%d.%m.%Y')
END = DT.strptime('07.09.2023', '%d.%m.%Y')
def get_random_date(start=START, end=END):
    delta = end - start
    return start + timedelta(random.randint(0, delta.days))


class Command(BaseCommand):
    help = 'Creates fake products'

    def add_arguments(self, parser):
        parser.add_argument('number', type=int, help='how many products needed')

    def handle(self, *args, **kwargs):
        number = kwargs['number']
        for i in range(1, number + 1):
            product = Product(product_name=f'Product{i}',
                            description=f'What a wonderful product {i}!',
                            price=Decimal(random.randint(1,100)),
                            quantity = random.randint(0,15),
                            date_of_addition=get_random_date())
            product.save()
        return f'{number} fake products created'