import json
from distutils.util import strtobool

from webexample.serializers import serializer_pet
from django.core.management.base import BaseCommand
from webexample.models import Pets


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--has_photo', help='')

    def handle(self, *args, **options):
        has_photo = strtobool(options['has_photo']) if options['has_photo'] else None
        pets = Pets.get_pets(has_photo=has_photo)
        res = {'pets': []}
        for pet in pets:
            serializer = serializer_pet(pet)

            res['pets'].append(serializer)

        self.stdout.write(json.dumps(res, default=str))
