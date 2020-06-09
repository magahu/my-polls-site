from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def create(request):
    return render(request, 'polls/create.html')

@login_required
def index(request):
    return render(request, 'polls/index.html')