from django.urls import path

from master.views import SendAllView, SendSpecificView, ServerList, ServerDetail

urlpatterns = [
    path('send/', SendAllView.as_view()),
    path('send/<str:server_name>', SendSpecificView.as_view()),
    path('server/', ServerList.as_view()),
    path('server/<str:name>', ServerDetail.as_view()),
]
