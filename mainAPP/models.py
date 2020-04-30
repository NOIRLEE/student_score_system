from django.db import models


class SysManager(models.Model):
    name = models.CharField(max_length=64)
    auth_string = models.CharField(max_length=100)
    phone = models.CharField(max_length=150)
    email = models.CharField(max_length=50)

    class Meta:
        db_table = 'sys_manager'

class Students(models.Model):
    name = models.CharField(max_length=50)
    sex = models.CharField(max_length=50)
    class_id = models.CharField(max_length=50)
    student_id = models.CharField(max_length=50)
    auth_string = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    class Meta:
        db_table = 'students'

class Teachers(models.Model):
    name = models.CharField(max_length=50)
    auth_string = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    job_num = models.CharField(max_length=50)
    pic = models.CharField(max_length=255)
    email = models.CharField(max_length=50)

    class Meta:
        db_table = 'teacher'
class Subject(models.Model):
    name = models.CharField(max_length=50)
    teacher_id = models.IntegerField()


    class Meta:
        db_table = 'subject'


class Score(models.Model):
    student_id = models.IntegerField()
    subject_id = models.IntegerField()
    value = models.CharField(max_length=10)

    class Meta:
        db_table = 'score'

class StudentClass(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'student_class'