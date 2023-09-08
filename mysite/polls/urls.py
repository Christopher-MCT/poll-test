from django.urls import path

from django.views.generic import TemplateView
from . import views




app_name = 'polls'
urlpatterns = [
    
   
    path('', views.Home.as_view(), name = 'home'),
    path('main/', views.MainView.as_view(), name='main'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
   
   
]

