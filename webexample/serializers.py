from djangoProject import settings
from .models import Pets


def serializer_pets(pets, many=True):

    return [
        {'id': pet.id, 'title': pet.title, 'name': pet.pet, 'age': pet.age, 'type': pet.type,
         'created': pet.created_at,  'images': pet.photos.url if pet.photos else None}
        for pet in pets
    ]


def serializer_pet(pet):
    pet_images = []
    for image in pet.images:
        pet_images.append(image.image.url)
    return {'id': pet.id, 'title': pet.title, 'name': pet.pet, 'age': pet.age, 'type': pet.type, 'created': pet.created_at,
            'images': pet_images}



def serializer_photo(pet):
    pet_images = []
    for image in pet.images:
        pet_images.append(image.image.url)
    return [
        {'id': pet.id, 'url': pet_images}
    ]
