from django.urls import path

from .views import *


urlpatterns = [
    path('student/', StudentListView.as_view()),
]
