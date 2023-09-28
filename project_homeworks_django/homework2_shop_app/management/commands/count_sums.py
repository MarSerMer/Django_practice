from django.core.management.base import BaseCommand
from homework2_shop_app.models import Order

class Command(BaseCommand):
    help = 'Counts sums of fake orders'

    def handle(self, *args, **kwargs):
        list_of_orders = Order.objects.all()
        for ord in list_of_orders:
            list_of_prods = ord.products.all()
            res = 0
            for prod in list_of_prods:
                res += prod.price
            ord.sum_of_order = res
            ord.save()
        return 'Sums of fake orders counted'