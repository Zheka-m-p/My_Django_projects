from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from . models import Task

# ------------------------------------------------------------
# ToDo list
# ------------------------------------------------------------

class TaskListView(ListView):
    model = Task
    template_name = 'to_do_list/to_do_home.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            queryset = Task.objects.filter(user=self.request.user)
            search_query = self.request.GET.get('q', '').strip()
            if search_query:
                queryset = queryset.filter(
                    Q(title__icontains=search_query) | Q(description__icontains=search_query)
                )
            return queryset
        return Task.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # берём стандартный конверт (там уже есть tasks)
        tasks = context['tasks']  # это уже queryset из get_queryset # достаём список задач
        context['total_tasks'] = tasks.count() # кладём общее количество
        context['incomplete_tasks'] = tasks.filter(complete=False).count()  # кладём количество невыполненных задач
        return context


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'to_do_list/task_create.html'
    fields = ['title', 'description']
    success_url = reverse_lazy('todo:to_do_home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'to_do_list/task_detail.html'
    context_object_name = 'task'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']   # '__all__' заменён на явный список
    success_url = reverse_lazy('todo:to_do_home')
    template_name = 'to_do_list/task_update.html'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('todo:to_do_home')
    template_name = 'to_do_list/task_delete.html'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


# ------------------------------------------------------------
# Быстрое переключение статуса задачи
# ------------------------------------------------------------

def toggle_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.complete = not task.complete  # переключаем True/False
    task.save()
    return redirect('todo:to_do_home')