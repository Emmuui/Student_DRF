from django.urls import path

from .views import *


urlpatterns = [
    path('student/', StudentListView.as_view()),

    path('mark/all', MarkListView.as_view()),
    path('mark/detail/<int:pk>', StudentMarkDetailView.as_view()),

    path('group/all', GroupsListView.as_view()),
    path('group/detail/<int:pk>', GroupsDetailView.as_view()),
    path('group/new', GroupsCreateView.as_view()),
    path('group/update/<int:pk>', GroupsUpdateView.as_view()),
]
