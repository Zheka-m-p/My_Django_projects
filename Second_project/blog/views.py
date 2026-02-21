from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from . models import Post, Comment
from . forms import CommentForm
from django.urls import reverse, reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin # 🔹 Импортируем миксин и ниже ошибку
from django.core.exceptions import PermissionDenied


# Create your views here.
def index(request):
    return render(request, 'blog/simple_home_blog.html')


class PostListView(ListView):
    model = Post
    template_name = 'blog/all_posts.html'
    context_object_name = 'posts' # имя переменной для шаблонов (все посты - список)
    ordering = ['-created_at']

    def get_queryset(self): # для фильтрации данных по названию и username автора
        queryset = super().get_queryset()

        title = self.request.GET.get('title')
        author = self.request.GET.get('author')

        if title:
            queryset = queryset.filter(title__icontains=title)
        if author:
            queryset = queryset.filter(author__username__icontains=author)

        return queryset


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/solo_post.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем пустую форму в контекст, чтобы вывести её в шаблоне
        context['comment_form'] = CommentForm()
        return context


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'blog/update_post.html'
    context_object_name = 'post'
    fields = ['title', 'content']

    def dispatch(self, request, *args, **kwargs):
        post = self.get_object()
        if post.author != request.user:
            raise PermissionDenied("Вы не можете редактировать этот пост.")
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('blog:solo_post', kwargs={'pk': self.object.pk })


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'

    def dispatch(self, request, *args, **kwargs):
        post = self.get_object()
        if post.author != request.user:
            raise PermissionDenied("Вы не можете удалить этот пост.")
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('blog:all_post_by_one_author', kwargs={'pk': self.object.author.pk})


class PostListViewByOneAuthor(ListView):
    model = Post
    template_name = 'blog/all_post_by_one_author.html'
    context_object_name = 'posts'
    ordering = ['-updated_at']


    def get_queryset(self):
        author_id = self.kwargs['pk']  # ← id автора из URL
        queryset = Post.objects.filter(author_id=author_id)

        title = self.request.GET.get('title') # 🔹 фильтрация по названию и автору
        author = self.request.GET.get('author')

        if title:
            queryset = queryset.filter(title__icontains=title)
        if author:
            queryset = queryset.filter(author__username__icontains=author)

        return queryset


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/create_post.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('blog:home')

    def form_valid(self, form):
        # Автоматически привязываем текущего юзера к посту
        form.instance.author = self.request.user
        return super().form_valid(form)


class CommentCreateView(LoginRequiredMixin, CreateView):
    ''' Вьюха для СОЗДАНИЯ комментария'''
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.author = self.request.user # Привязываем текущего юзера к комментарию
        # Берем id поста из URL и привязываем коммент к этому посту
        form.instance.post = get_object_or_404(Post, pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        # После отправки возвращаем юзера на страницу того же поста
        return reverse_lazy('blog:solo_post', kwargs={'pk': self.kwargs['pk']})


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    '''Вьюха для УДАЛЕНИЯ комментария'''
    model = Comment
    # Можно использовать твой готовый шаблон для удаления
    template_name = 'blog/delete_post.html'

    def dispatch(self, request, *args, **kwargs):
        comment = self.get_object()
        # ПРОВЕРКА ПРАВ: Если ты автор коммента ИЛИ автор поста — удалять можно
        if comment.author == request.user or comment.post.author == request.user:
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied("Нельзя удалять чужие комментарии!")

    def get_success_url(self):
        # После удаления возвращаемся на страницу поста
        return reverse_lazy('blog:solo_post', kwargs={'pk': self.object.post.pk})