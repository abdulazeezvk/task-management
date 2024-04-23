from django.urls import path
from .import views

app_name='managerapp'

urlpatterns = [
    path('',views.account,name='account'),
    path('index/',views.index,name="index"),

        #  ---------CreateTask------
    # path('Create-Task', views.CreateTask, name="Create-Task"),

    # path('user-logout', views.user_logout, name="user-logout"),
]

