"""polls URL Configuration"""

from django.urls import path
from . import views

urlpatterns = [
    path(
        route='home/',
        view=views.home,
        name='home'
    ),
    path(
        route='create-question/',
        view=views.create_question,
        name='create-question'
    ),
    path(
        route='<int:question>/create-choices/',
        view=views.create_choices,
        name='create-choices'
    ),
    path(
        route='index/',
        view=views.index,
        name='index'
    ),
]