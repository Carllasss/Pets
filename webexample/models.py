from django.db import models
from django.db.models import Prefetch

# Create your models here
class Pets(models.Model):
    title = models.CharField(verbose_name='Название', max_length=50)
    pet = models.TextField('Описание')
    age = models.CharField('Возраст', max_length=4)
    type = models.CharField('Тип', max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    photos = models.ImageField(upload_to='images', blank=True, null=True)


    def __str__(self):
        return self.title

    @staticmethod
    def get_pets(has_photo=None, offset=0, limit=20):
        if has_photo is None:
            pets = Pets.objects.all()[offset:offset + limit]
            for pet in pets:
                pet.images = list(Photo.objects.filter(Pet_id=pet.id).all())
        elif has_photo:
            pets = Pets.objects.exclude(photo__image__isnull=True)[offset:offset + limit]
            for pet in pets:
                pet.images = list(Photo.objects.filter(Pet_id=pet.id).all())
        else:
            pets = Pets.objects.exclude(photo__image__isnull=False)[offset:offset + limit]
            for pet in pets:
                pet.images = list(Photo.objects.filter(Pet_id=pet.id).all())

        for pet in pets:
            print(pet.photo.values('image'))
        return pets

    class Meta:
        verbose_name = 'Питомец'
        verbose_name_plural = 'Питомцы'


class Photo(models.Model):
    Pet = models.ForeignKey(
        Pets,
        on_delete=models.CASCADE,
        related_name='photo'
    )
    image = models.ImageField(upload_to='images', blank=True, null=True)

    def __str__(self):
        return str(self.image)

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'