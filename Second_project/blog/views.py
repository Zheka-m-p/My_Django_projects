from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from . models import Post
from django.urls import reverse, reverse_lazy


# Create your views here.
def index(request):
    return render(request, 'blog/simple_home_blog.html')


class PostListView(ListView):
    model = Post
    template_name = 'blog/all_posts.html'
    context_object_name = 'posts' # имя переменной для шаблонов (все посты - список)
    ordering = ['-created_at']


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/solo_post.html'
    context_object_name = 'post'


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'blog/update_post.html'
    context_object_name = 'post'
    fields = ['title', 'content']

    def get_success_url(self):
        return reverse_lazy('blog:solo_post', kwargs={'pk': self.object.pk })


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'

    def get_success_url(self):
        return reverse_lazy('blog:all_post_by_one_author', kwargs={'pk': self.object.author.pk})


class PostListViewByOneAuthor(ListView):
    model = Post
    template_name = 'blog/all_post_by_one_author.html'
    context_object_name = 'posts'
    ordering = ['-updated_at']

    def get_queryset(self):
        author_id = self.kwargs['pk']  # ← id автора из URL
        return Post.objects.filter(author_id=author_id)