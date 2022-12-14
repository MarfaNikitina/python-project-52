from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.utils.translation import gettext as _
from django_filters.views import FilterView
from task_manager.messages import TASK_CREATE_MESSAGE, \
    TASK_UPDATE_MESSAGE, TASK_DELETE_MESSAGE
from tasks.filter import TaskFilter
from tasks.forms import TaskForm
from tasks.models import Task
from task_manager.mixins import MyLoginRequiredMixin, TaskPassesTestMixin


class TaskListView(FilterView):
    model = Task
    fields = ['id', 'name', 'status',
              'author', 'executor', 'time_create']
    template_name = 'lists/task.html'
    filterset_class = TaskFilter


class TaskCreateView(MyLoginRequiredMixin,
                     SuccessMessageMixin,
                     CreateView):
    form_class = TaskForm
    model = Task
    template_name = 'edit.html'
    login_url = 'login'
    extra_context = {'title': _('Create task'),
                     'button_text': _('Create')}
    success_message = TASK_CREATE_MESSAGE
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskUpdateView(MyLoginRequiredMixin,
                     SuccessMessageMixin,
                     UpdateView):
    model = Task
    form_class = TaskForm
    login_url = 'login'
    template_name = 'edit.html'
    extra_context = {'title': _('Update task'),
                     'button_text': _('Update')}
    success_message = TASK_UPDATE_MESSAGE
    success_url = reverse_lazy('tasks')


class TaskDeleteView(TaskPassesTestMixin,
                     MyLoginRequiredMixin,
                     SuccessMessageMixin,
                     DeleteView):
    model = Task
    login_url = 'login'
    template_name = 'tasks/delete_task.html'
    success_url = reverse_lazy('tasks')
    success_message = TASK_DELETE_MESSAGE


class TaskDetail(MyLoginRequiredMixin, DetailView):
    template_name = 'tasks/detail_task.html'
    model = Task
