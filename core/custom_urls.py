from django.urls import path
from .views import courses, index, contact, product
# OR "from .views import *", adding all functions.

urlpatterns = [
    path('', index, name='index'),
    path('contact', contact, name='contato'),
    path('courses', courses, name='cursos'),
    path('product/<int:pk>', product, name='xuxa')
]