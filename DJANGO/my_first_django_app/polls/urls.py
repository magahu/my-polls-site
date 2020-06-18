"""polls URL Configuration"""

from django.urls import path
from . import views

urlpatterns = [

    path(route='hello-world', 
        view=views.hello_world,
        name='index'
        ),

    path(route='',
        view=views.index,
        name='index'
        ),

    path(route='<int:question_id>',
        view=views.detail,
        name='detail'
        ),

    path(route='<int:question_id>',
        view=views.results,
        name='results'
        ),

    path(route='<int:question_id>/vote/',
        view=views.vote,
        name='vote'
        )

    #path('<int:question_id>/results/', views.results, name='results'),
    #path('<int:question_id>/vote/', views.vote, name='vote'),
]