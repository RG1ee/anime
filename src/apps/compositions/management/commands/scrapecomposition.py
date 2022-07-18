import os.path

from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify
import requests as req

from apps.compositions.models import Composition


class Command(BaseCommand):
    help = "This command will scrape all japan compositions from source"

    def handle(self, *args, **kwargs):
        url = "https://ghibliapi.herokuapp.com/films"
        # get all films from ghibli api
        films = req.get(url).json()
        for film in films:
            # get title, description and image url from film
            title, description, image = film['title'], film['description'], film['image']
            composition = Composition(name=title, description=description)

            # get image from image url
            img_tmp = NamedTemporaryFile(delete=True)
            for chunk in req.get(image).iter_content(1024):
                img_tmp.write(chunk)
            img_tmp.flush()

            # save image
            filename = f"{slugify(title)}{os.path.splitext(image)[-1]}"
            composition.image.save(filename, File(img_tmp), save=True)
