from django.urls import path
from todo import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:pk>', views.delete_task, name='delete'),
    path('update/<int:pk>', views.update_task, name='update')
]