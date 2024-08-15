from django.urls import path

from task_runner2.views import Runner


urlpatterns = [
    path('', Runner.as_view()),
]
