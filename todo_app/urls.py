from django.urls import path

from todo_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('list/', views.TaskListview.as_view(), name='list'),
]