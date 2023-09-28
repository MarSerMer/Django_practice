from django.core.management.base import BaseCommand

from s2_blog_app.models import Author

class Command(BaseCommand):
    help = "Deleting one author by entering his/her id"

    def add_arguments(self, parser):
        parser.add_argument('pk', type = int, help = "Author's id")

    def handle(self,*args,**kwargs):
        pk = kwargs['pk']
        author = Author.objects.filter(pk=pk).first()
        author.delete()
        self.stdout.write(f'Deleted: {author}')