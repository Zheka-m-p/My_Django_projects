from django.urls import path
from . import views


app_name = 'feedback' # чисто название, может быть любым, для удобства навигации по url-ам

urlpatterns = [
    path('done/', views.done, name='done'),
    path('', views.index, name='home'),

]
