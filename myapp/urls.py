from django.urls import path
from . import views
urlpatterns = [
    path('', views.hello),
    path('about/', views.about),
    path('projects/', views.projects),
    path('projects/<int:id>', views.project),
    path('tasks/', views.tasks),
    path('tasks/<int:id>', views.task),
]