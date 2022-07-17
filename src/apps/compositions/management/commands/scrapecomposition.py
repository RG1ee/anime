import requests as req

from django.core.management.base import BaseCommand

from apps.compositions.models import Composition


class Command(BaseCommand):
    help = "This command will scrape all japanise compositions from source"

    def handle(self, *args, **kwargs):
        url = "https://ghibliapi.herokuapp.com/films"
        films = req.get(url).json()
        for film in films:
            title, description, image = film['title'], film['description'], film['image']
            filename = f"{title.replace(' ', '_')}.jpg"
            with open(filename, "wb") as file:
                response = req.get(image) 
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            Composition.objects.create(
                name=title, description=description,
                image=filename
            )

            
