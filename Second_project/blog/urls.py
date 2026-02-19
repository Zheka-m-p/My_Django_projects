from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='home'),
    # с постами связанное: все посты, плюс CRUD
    path('all_posts/', views.PostListView.as_view(), name='all_posts'),
    path('all_post_by_one_author/<int:pk>/', views.PostListViewByOneAuthor.as_view(), name='all_post_by_one_author'),

    path('post/<int:pk>/', views.PostDetailView.as_view(), name='solo_post'),
    path('update_post/<int:pk>/', views.PostUpdateView.as_view(), name='update_post'),
    path('delete_post/<int:pk>/', views.PostDeleteView.as_view(), name='delete_post'),


]