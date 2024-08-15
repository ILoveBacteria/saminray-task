from django.urls import path

from task_runner1.views import Runner


urlpatterns = [
    path('', Runner.as_view()),
]
