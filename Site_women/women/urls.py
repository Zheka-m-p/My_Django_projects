from django.urls import path, re_path, register_converter
from . import views
from . import converters

# noinspection PyTypeChecker
register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.index, name='home'), # http//127.0.0.1:800/
    path('cats/<int:cat_id>/', views.categories, name='cats_id'), # http//127.0.0.1:800/cats/2
    path('cats/<slug:cat_slug>/', views.categories_by_slug, name='cats_slug'), # http//127.0.0.1:800/cats/dd22

    path('archive/<year4:year>/', views.archive, name='archive'),
    # re_path(r'^archive/(?P<year>[0-9]{4})/', views.archive, name='archive'),

]