"""users Views"""

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import SignupForm
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from polls.models import Question
#class-based views
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


def signup(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SignupForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            confirmation = form.cleaned_data['confirmation']

            if password == confirmation:
                try:
                    user = User.objects.create_user(username=username, password=password)
                     # redirect to a new URL:
                    return redirect('users:login')
                except IntegrityError:
                    # Always return an HttpResponseRedirect after successfully dealing
                    # with POST data. This prevents data from being posted twice if a
                    # user hits the Back button.
                    return redirect('users:signup')
        
        else:
            return render(request, 'users/signup.html', {'form':form, 'error_message':'Los datos no se salvaron porque no eran validos'})

    
    return render(request, 'users/signup.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            # Redirect to a success page.
            return redirect('polls:home')
        else:
            # No backend authenticated the credentials
            return render(request, 'users/login.html')
    return render(request, 'users/login.html')
  
  
@login_required
def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return redirect('users:login')


class ProfileView(generic.DetailView, LoginRequiredMixin):
    template_name = 'users/profile.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['questions'] = Question.objects.filter(user=user).order_by('-pub_date')
        return context
