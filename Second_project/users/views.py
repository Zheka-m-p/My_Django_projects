from django.shortcuts import render, HttpResponse
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy


# Create your views here.
def pass_home(request):
    return render(request, 'users/pass_home.html')

class UserRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'users/register_user.html'
    success_url = reverse_lazy('main:main_page') # куда перекинет после успешной регистрации

class UserLoginView(LoginView):
    template_name = 'users/login_user.html'
    next_page = 'main:main_page' # куда перейти после авторизации



class UserLogoutView(LogoutView):
    next_page = 'main:main_page'  # куда перейти после выхода

