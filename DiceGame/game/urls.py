from django.urls import path
from .views import random_image

urlpatterns = [
    path('', random_image, name='random_image')
]
