from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from . import views




app_name = 'polls'
urlpatterns = [
    
   
    path('', views.Home.as_view(), name = 'home'),
    path("accounts/login/", views.LoginView.as_view(), name='register'),
    path("accounts/logout/", views.LoginView.as_view(), name='log-out'),
    path('main/', views.MainView.as_view(), name='main'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
 
#accounts/login/ [name='login']
#accounts/logout/ [name='logout']
#accounts/password_change/ [name='password_change']
#accounts/password_change/done/ [name='password_change_done']
#accounts/password_reset/ [name='password_reset']
#accounts/password_reset/done/ [name='password_reset_done']
#accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
#accounts/reset/done/ [name='password_reset_complete']
   
]

