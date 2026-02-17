from django.urls import path
from . import views


app_name = 'feedback' # чисто название, может быть любым, для удобства навигации по url-ам

urlpatterns = [
    path('', views.index, name='home'),
    # path('hello/', views.hello, name='hello'),

]
