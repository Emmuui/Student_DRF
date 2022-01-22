from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework import viewsets, status

from .models import Student
from .serializers import StudentSerializer, CreateStudentSerializer


class StudentViewSet(viewsets.ViewSet):

    def list(self, request):
        student = Student.objects.all()
        serializers = StudentSerializer(student, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = Student.objects.all()
        student = get_object_or_404(queryset, pk=pk)
        serializers = StudentSerializer(student)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        queryset = Student.objects.get(pk=pk)
        serializers = CreateStudentSerializer(queryset, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
