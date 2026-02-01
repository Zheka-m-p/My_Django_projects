from django.urls import path
from .views import index
# from . import views # - если потом пригодится много функций представлений

app_name = 'blog'

urlpatterns = [
    path('', index, name='home'),

]
