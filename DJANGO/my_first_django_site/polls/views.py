from django.shortcuts import render, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Question, Choice
from django.utils import timezone
from django.http import HttpResponseRedirect


def home(request):
    return render(request, 'polls/home.html')


def create_question(request):
    if request.method == 'POST':
        #import pdb; pdb.set_trace()
        if request.POST['question_text']:
            question_text = request.POST['question_text']
            pub_date =timezone.now()
            question = Question.objects.create(question_text=question_text, pub_date=pub_date)
            return render(request, 'polls/create_choices.html', {'question':question})

    return render(request, 'polls/create.html')


def create_choices(request, question):
    question = get_object_or_404(Question, pk=question)
    if request.method == 'POST':
        if request.POST['choice_text']:
            q = request.POST['question']
            text = request.POST['choice_text']
            question.choice_set.create(question=q, choice_text=text, votes=0)
            choices = question.choice_set.all()
            return render(request, 'polls/create_choices.html', {'question':question, 'choices':choices})
    
    return render(request, 'polls/create_choices.html', {'question':question} )


def index(request):
    return render(request, 'polls/index.html')