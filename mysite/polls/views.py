
from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Choice, NewUser
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, LogoutView
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
    

class ResultView(generic.DetailView):
    model =   Question
    template_name = 'polls/results.html'


##NEW LINES

#class votes(generic.ListView):

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
        
class CreatePollView(TemplateView):
      template_name = "polls/create_poll.html"
  
    
    
class SignUpView(CreateView):
    model= NewUser
    form_class = SignupForm
    template_name = 'usuarios/forms.html'

    def form_valid(self, form):
         """
         En este parte, si el formulario es valido guardamos lo que se obtiene de
          él y usamos authenticate para que el usuario incie sesión luego de 
          haberse registrado y lo redirigimos al index
         """
         form.save()
         usuario= form.cleaned_data.get('username')
         password = form.cleaned_data.get('password1')
         usuario = authenticate(username=usuario, password=password )
         login(self.request, usuario)
         return redirect('/')

class SignInView(LoginView):
     template_name = 'usuarios/login_user.html'

class SignOutView(LogoutView):
    pass