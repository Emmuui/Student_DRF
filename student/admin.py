from django.contrib import admin
from .models import *


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('name', 'dean')


@admin.register(Groups)
class GroupsAdmin(admin.ModelAdmin):
    list_display = ('name', 'faculty')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'second_name', 'mark_exams', 'group', 'scholarship')


@admin.register(Discipline)
class DisciplineAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Marks)
class MarksAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'mark')

