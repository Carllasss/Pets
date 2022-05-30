
from django.urls import path

from .views import PetlistView, PhotoView, PetView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('pets', PetlistView.as_view(), name='pets'),
    path('pets/<int:id>', PetView.as_view(), name='pet'),
    path('pets/<int:id>/photo', PhotoView.as_view(), name='photo')
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)