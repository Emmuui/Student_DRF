# from django.shortcuts import render
from .permissions import IsUserOrAdmin
from rest_framework.permissions import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from .serializers import *
from rest_framework import status, generics, viewsets


class IsUser(BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class Logout(APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class FacultyListView(generics.ListAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer


class FacultyDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer


class GroupsListView(generics.ListAPIView):
    queryset = Groups.objects.all()
    serializer_class = GroupsSerializer


class GroupsCreateView(generics.CreateAPIView):
    permission_classes = [IsUserOrAdmin]
    queryset = Groups.objects.all()
    serializer_class = CreateGroupSerializer


class GroupsUpdateView(generics.UpdateAPIView):
    permission_classes = [IsUserOrAdmin]
    queryset = Groups.objects.all()
    serializer_class = CreateGroupSerializer


class GroupsDetailView(generics.RetrieveDestroyAPIView):
    permission_classes = [IsUserOrAdmin]
    queryset = Groups.objects.all()
    serializer_class = CreateGroupSerializer


class StudentListView(generics.ListAPIView):
    permission_classes = (IsUser, )
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentCreateView(generics.CreateAPIView):
    permission_classes = [IsUserOrAdmin]
    queryset = Student.objects.all()
    serializer_class = CreateStudentSerializer


class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsUserOrAdmin]
    queryset = Student.objects.all()
    serializer_class = CreateStudentSerializer


class MarkListView(generics.ListAPIView):
    queryset = Marks.objects.all()
    serializer_class = MarkSerializer


class StudentMarkDetailView(APIView):

    def get(self, request, pk, format=None):
        mark = Marks.objects.filter(student=pk)
        serializer = MarkSerializer(mark, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
