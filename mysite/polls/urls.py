from django.urls import path

from django.views.generic import TemplateView
from . import views




app_name = 'polls'
urlpatterns = [
    
   
    path('', views.Home.as_view(), name = 'home'),
    path('home/', views.Home.as_view(), name = 'home'),
   # path('register/', views.SignUpView.as_view(), name = 'register'),
    path('registrate_sesion/', views.SignUpView.as_view(), name='register'),
    path('inicia_sesion/', views.SignInView.as_view(), name='sign_in'),
    path('cerrar_sesion', views.SignOutView.as_view(), name='sign_out'),
    path('main/', views.MainView.as_view(), name='main'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('create_Polls/', views.CreatePollView.as_view(), name='createPoll'),
   
   
]

