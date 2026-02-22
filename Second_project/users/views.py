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
    # success_url = reverse_lazy('users:login_user') # куда перекинет после успешной регистрации

    def get_success_url(self):
        '''Вытаскивает 'next' из ссылки, если он там есть.
        Если есть, отправляет на логин и пробрасывает 'next' дальше'''

        # Берем next сначала из POST (скрытое поле), потом из GET (URL)
        next_url = self.request.POST.get('next') or self.request.GET.get('next')
        if next_url:
            return f"{reverse_lazy('users:login_user')}?next={next_url}"
        return reverse_lazy('users:login_user')

class UserLoginView(LoginView):
    template_name = 'users/login_user.html'
    # убрал next_page, чтобы переходило на ту же страницу, где и был, перед входом
    # next_page = 'main:main_page' # куда перейти после авторизации


class UserLogoutView(LogoutView):
    pass # убрал next_page, чтобы переходило на ту же страницу, где и был, перед выходом
    # next_page = 'main:main_page'  # куда перейти после выхода
