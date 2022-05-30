from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views import View
from django.http import HttpResponse
import json
import requests

from .models import Pets, Photo
from .serializers import serializer_pets, serializer_pet, serializer_photo
from .forms import TaskForm, PhotoForm


# Create your views here.


class PetlistView(View):
    def get(self, request):
        limit = int(request.GET.get('limit', 20))
        offset = int(request.GET.get('offset', 0))

        pets = Pets.objects.all()[offset: offset + limit]

        return JsonResponse(dict(tasks=serializer_pets(pets)))

    def post(self, request):
        try:
            data = json.loads(request.body)

            form = TaskForm(data)
            if form.is_valid():
                pet_name = form.cleaned_data.get('pet')
                title_name = form.cleaned_data.get('title')
                age = form.cleaned_data.get('age')
                type_name = form.cleaned_data.get('type')
                new_pet = Pets(title=title_name, pet=pet_name, age=age, type=type_name)
                new_pet.save()
                return HttpResponse('success')
        except (requests.exceptions.JSONDecodeError, TypeError, ValueError):
            return JsonResponse(dict(error='invalid JSON'), status=400)

        return HttpResponse('success2')


class PetView(View):
    def get(self, request, id):
        pet = Pets.objects.filter(id=id).first()
        pet.images = list(Photo.objects.filter(Pet_id=pet.id).all())
        if not pet:
            return JsonResponse(dict(error='not pet'), status=404)
        return JsonResponse(dict(task=serializer_pet(pet)))

    def delete(self, request, id):
        pet = Pets.objects.filter(id=id)
        if not pet:
            return JsonResponse(dict(error='not pet'), status=404)
        pet.delete()
        return HttpResponse(id)


class PhotoView(View):
    def get(self, request, id):
        pet = Pets.objects.filter(id=id).first()
        pet.images = list(Photo.objects.filter(Pet_id=pet.id).all())
        if not pet:
            return JsonResponse(dict(error='not pet'), status=404)
        return JsonResponse(dict(pet=serializer_photo(pet)))

    def post(self, request, id):
        print(id)

        try:
            data = json.loads(request.body)
            form = PhotoForm(data)
            pet = Pets.objects.filter(id=id).first()
            if not pet:
                return JsonResponse(dict(error='not pet'), status=404)
            if form.is_valid():

                url = str(form.cleaned_data.get('url'))

                photo = Photo(Pet_id=id, image=url)

                photo.save()


                return JsonResponse(dict(pet=serializer_photo(photo)))
        except (requests.exceptions.JSONDecodeError, TypeError, ValueError):
            return JsonResponse(dict(error='invalid JSON'), status=400)
        return HttpResponse('not success')

