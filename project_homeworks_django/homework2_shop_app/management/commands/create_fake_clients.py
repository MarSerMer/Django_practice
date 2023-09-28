from django.core.management.base import BaseCommand
import random
from datetime import datetime as DT
from datetime import timedelta
from homework2_shop_app.models import Client

START = DT.strptime('01.01.1977', '%d.%m.%Y')
END = DT.strptime('01.01.2001', '%d.%m.%Y')
def get_random_date(start=START, end=END):
    delta = end - start
    return start + timedelta(random.randint(0, delta.days))


class Command(BaseCommand):
    help = 'Creates fake clients'

    def add_arguments(self, parser):
        parser.add_argument('number', type=int, help='how many clients needed')

    def handle(self, *args, **kwargs):
        number = kwargs['number']
        for i in range(1, number + 1):
            if i>=10:
                nt = 2
            else:
                nt = i
            client = Client(client_name=f'Name{i}',
                            email=f'mail{i}@iii.ff',
                            phone=f'+7-{nt}{nt}{nt}-{nt}{nt}',
                            address = f'Street{i} house {i+i}',
                            date_of_reg=get_random_date())
            client.save()
        return f'{number} fake clients created'
