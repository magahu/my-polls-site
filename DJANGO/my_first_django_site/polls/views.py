"""polls Views"""

from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Question, Choice, Vote
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.db import IntegrityError
#class-based views
from django.views import generic


def home(request):
    return render(request, 'polls/home.html')


def create_question(request):
    if request.method == 'POST':
        #import pdb; pdb.set_trace()
        if request.POST['question_text']:
            user_pk = request.POST['user']
            user = User.objects.get(pk=user_pk)
            question_text = request.POST['question_text']
            pub_date =timezone.now()
            question = Question.objects.create(user=user, question_text=question_text, pub_date=pub_date)
            return HttpResponseRedirect(reverse('polls:create-choices', args=(question.id,)))

    return render(request, 'polls/create.html')


@login_required
def create_choice(request, question):
    question = get_object_or_404(Question, pk=question)
    if request.method == 'POST':
        if request.POST['choice_text']:
            q = request.POST['question']
            text = request.POST['choice_text']
            question.choice_set.create(question=q, choice_text=text, votes=0)
            return HttpResponseRedirect(reverse('polls:create-choices', args=(question.id,)))
            
    return render(request, 'polls/choices.html', {'question':question})



#def index(request):
#    polls = Question.objects.all().order_by('-pub_date')
#    return render(request, 'polls/index.html', {'polls':polls})


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'polls'

 
    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('pub_date')


#def detail(request, question):
#    question = get_object_or_404(Question, pk=question)
#    return render(request, 'polls/detail.html', {'question':question})

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


@login_required
def vote(request, question):
    question = get_object_or_404(Question, pk=question)
    user_pk = request.POST['user']
    user = User.objects.get(pk=user_pk)
    
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        vote = Vote.objects.filter(user=user, question=question, choice=selected_choice)
        if not vote:
            selected_choice.votes += 1
            selected_choice.save()
            vote = Vote.objects.create(user=user, question=question, choice=selected_choice)
            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.
            return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })

    except IntegrityError:
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "Ya has votado",
            })

    
        
    return render(request, 'polls/detail.html', {'question':question})


#def results(request, question):
#    question = get_object_or_404(Question, pk=question)
#    return render(request, 'polls/results.html', {'question':question})


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'