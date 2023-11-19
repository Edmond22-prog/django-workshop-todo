from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("create_task/", views.create_task, name="create-task"),
    path("finished_tasks/", views.retrieve_finished_tasks, name="finished-tasks"),
    path("unfinished_tasks/", views.retrieve_unfinished_tasks, name="unfinished-tasks"),
    path("deleted_tasks/", views.retrieve_deleted_tasks, name="deleted-tasks"),
    path("delete_task/<int:task_id>/", views.delete_task, name="delete-task"),
    path("finish_task/<int:task_id>/", views.finish_task, name="finish-task"),
]
