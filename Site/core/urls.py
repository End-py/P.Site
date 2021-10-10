
from django.urls import path
from django.conf.urls import handler404, handler500
from . import views
from .views import *


urlpatterns = [
    path('home', index),
    path('contato', contato),
    path('produto/<int:id>', produto, name='produto'),
    path('produtos/', produtos),
]

handler404 = views.error_404
handler500 = views.error_500
