from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('master/', include('master.urls')),
    path('task_assigner/', include('task_assigner.urls')),
    path('task_runner1/', include('task_runner1.urls')),
    path('task_runner2/', include('task_runner2.urls')),
    path('task_runner3/', include('task_runner3.urls')),
]
