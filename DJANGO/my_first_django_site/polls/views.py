from django.shortcuts import render, reverse, get_object_or_404, redirect
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
            return HttpResponseRedirect(reverse('polls:create-choices', args=(question.id,)))

    return render(request, 'polls/create.html')


def create_choice(request, question):
    question = get_object_or_404(Question, pk=question)
    if request.method == 'POST':
        if request.POST['choice_text']:
            q = request.POST['question']
            text = request.POST['choice_text']
            question.choice_set.create(question=q, choice_text=text, votes=0)
            return HttpResponseRedirect(reverse('polls:create-choices', args=(question.id,)))
            
    return render(request, 'polls/choices.html', {'question':question})



def index(request):
    polls = Question.objects.all().order_by('-pub_date')
    return render(request, 'polls/index.html', {'polls':polls})


def detail(request, question):
    question = get_object_or_404(Question, pk=question)
    return render(request, 'polls/detail.html', {'question':question})


def vote(request, question):
    question = get_object_or_404(Question, pk=question)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    return render(request, 'polls/detail.html', {'question':question})


def results(request, question):
    question = get_object_or_404(Question, pk=question)
    return render(request, 'polls/results.html', {'question':question})
