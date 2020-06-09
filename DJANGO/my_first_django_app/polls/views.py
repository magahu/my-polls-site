"""myapp Views"""

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from polls.models import Question

def hello_world(request):
    return HttpResponse("Hello, world! You're at at the polls index")

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')#[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'detail.html', {'question':question})

def results(request):
    pass

def vote(request):
    pass