from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django_filters.views import FilterView
from django.views import generic

from .models import Todo
from .forms import SignUpForm, TodoModelForm, TodoCompletedModelForm


@method_decorator(user_passes_test(lambda user: user.is_superuser or user.is_staff), name='dispatch')
class TodoCreateListView(SuccessMessageMixin, generic.CreateView, FilterView, generic.ListView):
    model = Todo
    paginate_by = 10
    form_class = TodoModelForm
    success_url = '/'
    context_object_name = 'tasks'
    template_name = 'todo/add_todo.html'
    filterset_fields = ['title', 'current_date']
    success_message = "Todo task has been added"

    def get_queryset(self):
        return self.model.objects.filter(is_complete=True)

    def get_context_data(self, **kwargs):
        context = super(TodoCreateListView, self).get_context_data(**kwargs)
        context['pending_tasks'] = Todo.objects.filter(is_complete=False)
        return context


def complete_todo_view(request, pk):
    todo = get_object_or_404(Todo, id=pk)
    is_complete = request.POST.get('is_complete', False)
    if is_complete == 'on':
        is_complete = True
    todo.is_complete = is_complete
    todo.save()
    return redirect('/')


def incomplete_todo_view(request, pk):
    todo = get_object_or_404(Todo, id=pk)
    is_complete = request.POST.get('is_complete', False)
    if is_complete == 'on':
        is_complete = False
    todo.is_complete = is_complete
    todo.save()
    return redirect('/')


@method_decorator(user_passes_test(lambda user: user.is_superuser or user.is_staff), name='dispatch')
class TodUpdateView(SuccessMessageMixin, generic.UpdateView):
    model = Todo
    success_url = '/'
    form_class = TodoCompletedModelForm
    template_name = 'todo/add_todo.html'
    success_message = "Todo task has been updated"


@method_decorator(user_passes_test(lambda user: user.is_superuser or user.is_staff), name='dispatch')
class TodoDeleteView(SuccessMessageMixin, generic.DeleteView):
    model = Todo
    success_url = '/'
    success_message = "The tasks has been deleted."
    template_name = 'common/delete_confirm.html'
