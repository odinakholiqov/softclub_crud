from django.urls import path
from .views import tasks_list, TaskDetail, NewTask, EditTask, DeleteTask

urlpatterns = [
    path("", tasks_list, name="tasks_list"),
    path("<int:pk>", TaskDetail.as_view(), name="task_detail"),
    path("<int:pk>/edit", EditTask.as_view(), name="task_edit"),
    path("<int:pk>/delete", DeleteTask.as_view(), name="task_delete"),
    
    
    path("new", NewTask.as_view(), name="new_task"),


    path("done/", tasks_list, name="tasks_done_list"),
    path("today/", tasks_list, name="tasks_today_list"),

]
