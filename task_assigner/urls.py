from django.urls import path

from task_assigner.views import Assigner


urlpatterns = [
    path('', Assigner.as_view(), name='assigner')
]
