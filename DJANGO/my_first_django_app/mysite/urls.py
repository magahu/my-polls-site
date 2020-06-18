"""mysite URL Configuration"""

from django.contrib import admin
from django.urls import path, include

app_name = 'polls'

urlpatterns = [

    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
