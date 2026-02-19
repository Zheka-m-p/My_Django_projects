from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.pass_home, name='pass_home'),
    path('register_user/', views.UserRegisterView.as_view(), name='register_user'),
    path('login_user/', views.UserLoginView.as_view(), name='login_user'),
    path('logout_user/', views.UserLogoutView.as_view(), name='logout_user'),

]