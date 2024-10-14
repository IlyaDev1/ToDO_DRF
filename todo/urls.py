from django.urls import path, include
import task_manager.urls as task_manager_urls


urlpatterns = [
    path('', include(task_manager_urls)),
]
