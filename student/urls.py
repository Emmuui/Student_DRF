from django.urls import path

from .views import *


urlpatterns = [
    path('student/all', StudentListView.as_view()),
    path('student/add', StudentCreateView.as_view()),
    path('student/detail/<int:pk>', StudentDetailView.as_view()),

    path('mark/all', MarkListView.as_view()),
    path('mark/detail/<int:pk>', StudentMarkDetailView.as_view()),

    path('faculty/all', FacultyListView.as_view()),
    path('faculty/detail/<int:pk>', FacultyDetailView.as_view()),

    path('group/all', GroupsListView.as_view()),
    path('group/detail/<int:pk>', GroupsDetailView.as_view()),
    path('group/new', GroupsCreateView.as_view()),
    path('group/update/<int:pk>', GroupsUpdateView.as_view()),
]
