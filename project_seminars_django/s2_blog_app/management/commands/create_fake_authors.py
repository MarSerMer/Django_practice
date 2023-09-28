import random
from datetime import datetime as DT
from datetime import timedelta
from django.core.management.base import BaseCommand

from s2_blog_app.models import Author

START = DT.strptime('01.01.1977', '%d.%m.%Y')
END = DT.strptime('01.01.2001', '%d.%m.%Y')
def get_random_date(start=START, end=END):
    delta = end - start
    return start + timedelta(random.randint(0, delta.days))

class Command(BaseCommand):
    help = "Creates fake authors to play and work with 's2_blog_app'"

    def add_arguments(self, parser):
        parser.add_argument('number', type = int, help = 'how many authors needed')

    def handle(self,*args,**kwargs):
        number = kwargs['number']
        for i in range (1, number+1):
            author = Author(first_name = f'Firstname{i}',
                            last_name = f'Lastname{i}',
                            email = f'mail{i}@iii.ff',
                            biography = f'Biography of Lastname{i}',
                            birthday = get_random_date())
            author.save()
        return f'{number} fake authors created'