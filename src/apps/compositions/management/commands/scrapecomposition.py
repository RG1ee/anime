import os.path

from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify
import requests as req

from src.apps.compositions.models import Composition


class Command(BaseCommand):
    help = "This command will scrape all japanise compositions from source"

    def handle(self, *args, **kwargs):
        url = "https://ghibliapi.herokuapp.com/films"
        films = req.get(url).json()
        for film in films:
            title, description, image = (
                film['title'], film['description'], film['image']
            )
            composition = Composition(name=title, description=description)

            img_tmp = NamedTemporaryFile(delete=True)
            for chunk in req.get(image).iter_content(1024):
                img_tmp.write(chunk)
            img_tmp.flush()

            filename = f"{slugify(title)}{os.path.splitext(image)[-1]}"
            composition.image.save(filename, File(img_tmp), save=True)
