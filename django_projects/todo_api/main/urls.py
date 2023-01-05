# from django.urls import path

# from main.views import tasks_list, task_detail, task_create, task_update, task_delete
#
# urlpatterns = [
#     path('tasks/', tasks_list),
#     path('tasks/<int:id>/', task_detail),
#     path('tasks-create/', task_create),
#     path('tasks-update/<int:pk>/', task_update),
#     path('tasks-delete/<int:pk>/', task_delete)
# ]

from django.urls import path

from main.views import TaskListCreateView, TaskDetailView

urlpatterns = [
    # class urls
    path('tasks/', TaskListCreateView.as_view()),
    path('tasks/<int:pk>/', TaskDetailView.as_view()),
]
