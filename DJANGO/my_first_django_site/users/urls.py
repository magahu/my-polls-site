"""users URL Configuration"""

from django.urls import path
from . import views

urlpatterns = [
    path(
        route='signup/',
        view=views.signup,
        name='signup'
        ),
    path(
    route='login/',
    view= views.login_view,
    name='login'
    ),
    path(
        route='logout/',
        view=views.logout_view,
        name='logout'
        ),
]
