from django.shortcuts import redirect, render

from core.forms import CreateTaskForm
from core.models import TodoTask


def index(request):
    todo_tasks = TodoTask.objects.filter(deleted=False).order_by("-updated_date")
    return render(request, "core/index.html", {"todo_tasks": todo_tasks})


def create_task(request):
    create_task_form = CreateTaskForm(request.POST)
    if create_task_form.is_valid():
        title = create_task_form.cleaned_data["title"]
        TodoTask.objects.create(title=title)

    return redirect("index")


def retrieve_finished_tasks(request):
    finished_tasks = TodoTask.objects.filter(completed=True).order_by(
        "-updated_date"
    )
    return render(
        request,
        "core/index.html",
        {"todo_tasks": finished_tasks, "status": "finished"},
    )


def retrieve_unfinished_tasks(request):
    unfinished_tasks = TodoTask.objects.filter(
        completed=False, deleted=False
    ).order_by("-updated_date")
    return render(
        request,
        "core/index.html",
        {"todo_tasks": unfinished_tasks, "status": "in_progress"},
    )


def retrieve_deleted_tasks(request):
    deleted_tasks = TodoTask.objects.filter(deleted=True).order_by("-updated_date")
    return render(
        request,
        "core/index.html",
        {"todo_tasks": deleted_tasks, "status": "deleted"},
    )


def delete_task(request, task_id):
    task = TodoTask.objects.get(id=task_id)
    task.deleted = True
    task.save()
    return redirect("index")


def finish_task(request, task_id):
    task = TodoTask.objects.get(id=task_id)
    task.completed = True
    task.save()
    return redirect("index")
