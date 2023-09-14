
from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Choice
#from django.contrib.auth import login, authenticate
#from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User


from django.urls import reverse
from django.views import generic
from django.views.generic import TemplateView, CreateView
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse

from .forms import SignupForm







class Home(TemplateView):
    template_name = 'polls/home.html'


class MainView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions"""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
    

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte = timezone.now())

   
def vote(request, question_id):
        question = get_object_or_404(Question, pk=question_id)
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
            return HttpResponseRedirect(reverse('polls:results', args=(question.id)))

class ResultView(generic.DetailView):
    model =   Question
    template_name = 'polls/results.html'


##NEW LINES



 
        
class CreatePollView(TemplateView):
      template_name = "polls/create_poll.html"
  
    
    
