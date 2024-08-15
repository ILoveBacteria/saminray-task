from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('master/', include('master.urls')),
    path('task_assigner/', include('task_assigner.urls')),
    path('task_runner1/', include('task_runner1.urls')),
    path('task_runner2/', include('task_runner2.urls')),
    path('task_runner3/', include('task_runner3.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
