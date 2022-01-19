# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework import status, generics


class GroupsListView(generics.ListAPIView):
    queryset = Groups.objects.all()
    serializer_class = GroupsSerializer


class GroupsCreateView(generics.CreateAPIView):
    queryset = Groups.objects.all()
    serializer_class = CreateGroupSerializer


class GroupsUpdateView(generics.UpdateAPIView):
    queryset = Groups.objects.all()
    serializer_class = CreateGroupSerializer


class GroupsDetailView(generics.RetrieveDestroyAPIView):
    queryset = Groups.objects.all()
    serializer_class = CreateGroupSerializer


class StudentListView(generics.ListAPIView):

    queryset = Student.objects.all()
    serializer_class = GroupsSerializer

    # def get(self, request, format=None):
    #     student = Student.objects.all()
    #     serializer = StudentSerializer(student, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)


class MarkListView(generics.ListCreateAPIView):
    queryset = Marks.objects.all()
    serializer_class = MarkSerializer


class StudentMarkDetailView(APIView):

    def get(self, request, pk, format=None):
        mark = Marks.objects.filter(student=pk)
        serializer = MarkSerializer(mark, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
