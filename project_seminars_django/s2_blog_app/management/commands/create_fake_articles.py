
import random
from datetime import datetime as DT
from datetime import timedelta
from django.core.management.base import BaseCommand

from s2_blog_app.models import Author, Article


START = DT.strptime('01.01.1977', '%d.%m.%Y')
END = DT.strptime('01.01.2001', '%d.%m.%Y')
def get_random_date(start=START, end=END):
    delta = end - start
    return start + timedelta(random.randint(0, delta.days))


class Command(BaseCommand):
    help = "Creates fake articles (random choice of author) to play and work with 's2_blog_app'"

    def add_arguments(self, parser):
        parser.add_argument('number', type = int, help = 'how many articles needed')

    def handle(self,*args,**kwargs):
        number = kwargs['number']
        list_of_authors = Author.objects.all()
        for i in range (1, number+1):
            author = random.choice(list_of_authors)
            is_publ = random.choice([True, False])
            if is_publ:
                date = get_random_date()
            else: date='1111-11-11'
            article = Article(author=author,
                              title=f'Title-{i}',
                              content=f'A big interesting text {i}',
                              date_of_publ=date,
                              category=random.choice(['Science','Art','Physics','Physiology']),
                              amount_of_views=random.randint(0,150),
                              is_published=is_publ)
            article.save()
        return f'{number} fake articles created'