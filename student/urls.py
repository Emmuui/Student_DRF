from django.urls import path
from rest_framework import routers

from rest_framework.routers import DefaultRouter

from . import views, api


urlpatterns = [
    path('student/all', views.StudentListView.as_view()),
    path('student/add', views.StudentCreateView.as_view()),
    path('student/detail/<int:pk>', views.StudentDetailView.as_view()),

    path('mark/all', views.MarkListView.as_view()),
    path('mark/detail/<int:pk>', views.StudentMarkDetailView.as_view()),

    path('faculty/all', views.FacultyListView.as_view()),
    path('faculty/detail/<int:pk>', views.FacultyDetailView.as_view()),

    path('group/all', views.GroupsListView.as_view()),
    path('group/detail/<int:pk>', views.GroupsDetailView.as_view()),
    path('group/new', views.GroupsCreateView.as_view()),
    path('group/update/<int:pk>', views.GroupsUpdateView.as_view()),

    path('viewsets/student/list', api.StudentViewSet.as_view({'get': 'list'})),
    path('viewsets/student/detail/<int:pk>', api.StudentViewSet.as_view({'get': 'retrieve'})),
    path('viewsets/student/update/<int:pk>', api.StudentViewSet.as_view({'put': 'update'})),
]

routers = DefaultRouter()
routers.register('modelviewsets/student_marks', api.MarksViewSet, basename='student_marks')
routers.register('modelviewsets/student', api.StudentModelViewSet, basename='student_model_view_set')
urlpatterns += routers.urls
