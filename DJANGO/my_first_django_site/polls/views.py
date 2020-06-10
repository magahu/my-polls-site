from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'polls/home.html')


def create(request):
    return render(request, 'polls/create.html')


def index(request):
    return render(request, 'polls/index.html')