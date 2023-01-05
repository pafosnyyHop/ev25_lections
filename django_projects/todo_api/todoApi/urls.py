
from django.contrib import admin
from django.urls import path, include

# from main.views import tasks_list, task_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('main.urls')),
    path('api/v1/accounts/', include('account.urls')),

]


