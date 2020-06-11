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
        view=views.create_choice,
        name='create-choices'
    ),
    path(
        route='index/',
        view=views.index,
        name='index'
    ),
    path(
        route='<int:question>/detail',
        view=views.detail,
        name='detail'
    ),
    path(
        route='<int:question>/vote',
        view=views.vote,
        name='vote'
    ),
    path(
        route='<int:question>/results',
        view=views.results,
        name='results'
    )
]