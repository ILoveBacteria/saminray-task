from django.urls import path

from master.views import SendAllView, SendSpecificView, NameServerList, NameServerDetail

urlpatterns = [
    path('send/', SendAllView.as_view()),
    path('send/<str:server_name>', SendSpecificView.as_view()),
    path('name_server/', NameServerList.as_view()),
    path('name_server/<str:name>', NameServerDetail.as_view()),
]
