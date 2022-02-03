from rest_framework import serializers
from .models import *
# from django.shortcuts import get_object_or_404


class DisciplineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Discipline
        fields = ['name', ]


class FacultySerializer(serializers.ModelSerializer):

    class Meta:
        model = Faculty
        fields = '__all__'


class GroupsSerializer(serializers.ModelSerializer):
    faculty = FacultySerializer()
    # faculty_id = serializers.IntegerField()

    class Meta:
        model = Groups
        fields = ['id', 'name', 'faculty']

    # def create(self, validated_data):
    #     faculty = get_object_or_404(Faculty, id=validated_data['faculty_id'])
    #     group = Groups.objects.create(
    #         name=validated_data['name'],
    #         faculty=faculty
    #     )
    #     group.save()
    #     faculty.save()
    #     return group


class CreateGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    group = GroupsSerializer()

    class Meta:
        model = Student
        fields = '__all__'


class CreateStudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'


class StudentMarkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['id', 'second_name']


class MarkSerializer(serializers.ModelSerializer):
    subject = DisciplineSerializer()
    student = StudentMarkSerializer()

    class Meta:
        model = Marks
        fields = ['student', 'subject', 'mark']

