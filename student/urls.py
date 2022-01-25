from django.urls import path, include
from rest_framework import routers
# from rest_framework.authtoken import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter

from .views import *
from .api import *

urlpatterns = [
    path('auth/', include('djoser.urls')),
    # path('auth/token', views.obtain_auth_token, name='token'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair_view'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh_view'),

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

    path('viewsets/student/list', StudentViewSet.as_view({'get': 'list'})),
    path('viewsets/student/detail/<int:pk>', StudentViewSet.as_view({'get': 'retrieve'})),
    path('viewsets/student/update/<int:pk>', StudentViewSet.as_view({'put': 'update'})),
]

routers = DefaultRouter()
routers.register('modelviewsets/student_marks', MarksViewSet, basename='student_marks')
routers.register('modelviewsets/student', StudentModelViewSet, basename='student_model_view_set')
urlpatterns += routers.urls
