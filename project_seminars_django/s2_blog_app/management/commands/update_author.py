from django.core.management.base import BaseCommand

from s2_blog_app.models import Author

class Command(BaseCommand):
    help = "Update last name of one author by entering his/her id"

    def add_arguments(self, parser):
        parser.add_argument('pk', type = int, help = "Author's id")
        parser.add_argument('name', type=str, help="Author's id")

    def handle(self,*args,**kwargs):
        pk = kwargs['pk']
        name = kwargs['name']
        author = Author.objects.filter(pk=pk).first()
        author.last_name = name
        author.save()
        self.stdout.write(f'Information: {author}')