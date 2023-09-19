
from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Question, Choice
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login

from django.views import View, generic
from django.views.generic import TemplateView
from django.utils import timezone
from django.http import HttpResponseRedirect







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
            return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

class ResultView(generic.DetailView):
    model =   Question
    template_name = 'polls/results.html'


##NEW LINES



class LoginView(View):
    template_name = 'registration/login.html'

    def get(self, request):
        # import pdb; pdb.set_trace()
        if request.user.is_authenticated:
            return redirect(reverse('polls:main'))
        else: 
            return render(request, self.template_name)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('main')  #  redirigir al usuario después de iniciar sesión.
        else:
            # Handle authentication failure (e.g., show an error message)
            return render(request, self.template_name, {'error_message': 'Invalid login credentials'})

        

def logout_view(request):
    logout(request)
    #redirigiendo al home
    return redirect(reverse('polls:home'))
 
    
