from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from statuses.forms import StatusForm
from statuses.models import Status
from django.utils.translation import gettext as _


class StatusListView(LoginRequiredMixin, ListView):
    model = Status
    template_name = 'lists/status_list.html'


class StatusCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = StatusForm
    model = Status
    template_name = 'create.html'
    extra_context = {
        'title': _('Создать статус'),
        'button_text': _('Создать')
    }

    def get_success_url(self):
        messages.success(self.request, _('Статус успешно создан'))
        return reverse_lazy('statuses')


class StatusUpdateView(LoginRequiredMixin, UpdateView):
    model = Status
    form_class = StatusForm
    template_name = 'update.html'
    extra_context = {
        'title': _('Изменение статуса'),
        'button_text': _('Изменить')
    }

    def get_success_url(self):
        messages.success(self.request, _('Статус успешно изменён'))
        return reverse_lazy('statuses')


class StatusDeleteView(LoginRequiredMixin, DeleteView):
    model = Status
    template_name = 'delete.html'
    extra_context = {
        'title': _('Удаление статуса')
    }

    def get_success_url(self):
        # messages.error(self.request, _('Невозможно удалить статус, потому что он используется'))
        messages.success(self.request, _('Статус успешно удален'))
        return reverse_lazy('statuses')
