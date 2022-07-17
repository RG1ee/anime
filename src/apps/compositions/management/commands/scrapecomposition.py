from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "This command will scrape all japanise compositions from source"

    def handle(self, *args, **kwargs):
        import this
