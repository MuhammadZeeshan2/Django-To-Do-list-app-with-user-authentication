from django.urls import path
from base import views
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView,RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [

   
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    # path('logout/', CustomLogoutView.as_view(), name='logout'),
     path('', TaskList.as_view(), name='tasks'),
    path('task/<slug:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<slug:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<slug:pk>/', TaskDelete.as_view(), name='task-delete'),
]
