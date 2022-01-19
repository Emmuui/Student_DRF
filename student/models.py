from django.db import models


class Faculty(models.Model):
    name = models.CharField(verbose_name='Название факультета', max_length=100)
    dean = models.CharField(verbose_name='Декан', max_length=100)

    class Meta:
        verbose_name = 'Факультет'
        verbose_name_plural = 'Факультеты'

    def __str__(self):
        return self.name


class Groups(models.Model):
    name = models.CharField(verbose_name='Название группы', max_length=100)
    faculty = models.ForeignKey(Faculty, verbose_name='Факультет', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(verbose_name='Имя студента', max_length=100)
    second_name = models.CharField(verbose_name='Фамилия студента', max_length=100)
    mark_exams = models.IntegerField(verbose_name='Оценка за экзамен')
    group = models.ForeignKey(Groups, verbose_name='Название группы', on_delete=models.CASCADE)
    scholarship = models.BooleanField(verbose_name='Стипендия', default=False)

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

    def __str__(self):
        return self.name


class Discipline(models.Model):
    name = models.CharField(verbose_name='Название дисциплины', max_length=100)

    class Meta:
        verbose_name = 'Дисциплина'
        verbose_name_plural = 'Дисциплины'

    def __str__(self):
        return self.name


class Marks(models.Model):
    student = models.ForeignKey(Student, verbose_name='Студент', on_delete=models.CASCADE, related_name='student_mark')
    subject = models.ForeignKey(Discipline, verbose_name='Дисциплина', on_delete=models.CASCADE)
    mark = models.IntegerField(verbose_name='Оценка')

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'

    def __int__(self):
        return self.mark
