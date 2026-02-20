from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='home'), # главная страница приложения
    # с постами связанное: все посты, посты одного автора
    path('all_posts/', views.PostListView.as_view(), name='all_posts'),
    path('all_post_by_one_author/<int:pk>/', views.PostListViewByOneAuthor.as_view(), name='all_post_by_one_author'),
    # плюс CRUD
    path('create_post/', views.PostCreateView.as_view(), name='create_post'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='solo_post'),
    path('update_post/<int:pk>/', views.PostUpdateView.as_view(), name='update_post'),
    path('delete_post/<int:pk>/', views.PostDeleteView.as_view(), name='delete_post'),



]