from django.shortcuts import render
from .models import Task
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView


def tasks_list(request):
    tasks = Task.objects.all()
    context = {"all_tasks": tasks}
    
    return render(request, "tasks/all_tasks.html", context)


class TaskDetail(DetailView):
    model = Task
    template_name = "tasks/task_detail.html"


class NewTask(CreateView):
    model = Task
    template_name = "tasks/new_task.html"
    fields = "__all__" 


class EditTask(UpdateView):
    model = Task
    template_name = "tasks/task_edit.html"
    fields = "__all__" 

class DeleteTask(DeleteView):
    model = Task
    template_name = "tasks/task_delete.html"
    success_url = reverse_lazy("tasks_list")
