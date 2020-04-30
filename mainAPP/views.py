from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from mainAPP.models import *
from common import make_pwd




class ManagerView(View):

    def get(self,request):
        if request.GET.get('id', ''):
            manager = SysManager.objects.get(pk=request.GET.get('id'))
            return JsonResponse({
                'id': manager.id,
                'name': manager.name,
                'auth_string': manager.auth_string,
                'phone': manager.phone,
                'email':manager.email

            })

        managers = SysManager.objects.all()
        return render(request, 'basic/user_manager/sys_manager_2.html', locals())
    def post(self,request):
        print(request.POST)
        id = request.POST.get('id', None)  # 注意： form表单页面不建议使用id 字段名
        name = request.POST.get('name')
        auth_string = request.POST.get('auth_string')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        # 验证是否为空(建议:页面上验证是否为空)

        if id:
            # 更新
            manager = SysManager.objects.get(pk=id)
            manager.name = name
            manager.auth_string =  make_pwd(auth_string)
            manager.phone = phone
            manager.email = email
            manager.save()
        else:
            pwd = make_pwd(auth_string)
            SysManager.objects.create(name=name,auth_string=pwd,email=email, phone=phone )

        return redirect('/sys_manager_2/')
    def delete(self,request):
        manager_id = request.GET.get('id')
        manager = SysManager.objects.get(pk=manager_id)
        manager.delete()

        return JsonResponse({
            'status': 0,
            'msg': '删除成功!'
        })

class StudentView(View):

    def get(self,request):
        if request.GET.get('student_id', ''):
            student_id = request.GET.get('student_id')
            students = Students.objects.raw('select students.id,students.name,students.sex,student_class.name as class_name,students.auth_string,students.phone,students.email from students  join student_class on students.class_id=student_class.id  where student_id = %s'%student_id)
            return render(request, 'basic/user_manager/sys_student.html', locals())

        students = Students.objects.raw('select students.id,students.name,students.sex,student_class.name as class_name,students.auth_string,students.phone,students.email from students  join student_class on students.class_id=student_class.id ;')
        return render(request, 'basic/user_manager/sys_student.html', locals())
    def post(self,request):
        print(request.POST)
        id = request.POST.get('id', None)  # 注意： form表单页面不建议使用id 字段名
        name = request.POST.get('name')
        sex = request.POST.get('sex')
        class_id = request.POST.get('class_id')
        student_id = request.POST.get('student_id')
        auth_string = request.POST.get('auth_string')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        # 验证是否为空(建议:页面上验证是否为空)

        if id:
            # 更新
            student = Students.objects.get(pk=id)
            student.name = name
            student.sex = sex
            student.class_id = class_id
            student.student_id = student_id
            student.auth_string =  make_pwd(auth_string)
            student.phone = phone
            student.email = email
            student.save()
        else:
            pwd = make_pwd(auth_string)
            Students.objects.create(name=name, sex=sex, class_id=class_id,student_id=student_id,auth_string=pwd, email=email, phone=phone)

        return redirect('/sys_student/')
    def delete(self,request):
        student_id = request.GET.get('id')
        student = Students.objects.get(pk=student_id)
        student.delete()

        return JsonResponse({
            'status': 0,
            'msg': '删除成功!'
        })
class TeacherView(View):

    def get(self,request):
        if request.GET.get('teacher_id', ''):
            teacher_id = request.GET.get('teacher_id')
            teachers = Students.objects.raw('select * from teacher where job_num = %s' % teacher_id)
            return render(request, 'basic/user_manager/sys_teacher.html', locals())

        teachers = Teachers.objects.all()
        return render(request, 'basic/user_manager/sys_teacher.html', locals())
    def post(self,request):
        print(request.POST)
        id = request.POST.get('id', None)  # 注意： form表单页面不建议使用id 字段名
        name = request.POST.get('name')
        auth_string = request.POST.get('auth_string')
        phone = request.POST.get('phone')
        job_num = request.POST.get('job_num')
        pic = request.POST.get('pic')
        email = request.POST.get('email')
        # 验证是否为空(建议:页面上验证是否为空)

        if id:
            # 更新
            teacher = Teachers.objects.get(pk=id)
            teacher.name = name
            teacher.auth_string =  make_pwd(auth_string)
            teacher.phone = phone
            teacher.job_num = job_num
            teacher.pic = pic
            teacher.email = email
            teacher.save()
        else:
            pwd = make_pwd(auth_string)
            Teachers.objects.create(name=name,  auth_string=pwd, email=email, phone=phone,job_num=job_num,pic=pic)

        return redirect('/sys_teacher/')
    def delete(self,request):
        teacher_id = request.GET.get('id')
        teacher = Teachers.objects.get(pk=teacher_id)
        teacher.delete()

        return JsonResponse({
            'status': 0,
            'msg': '删除成功!'
        })
class SubjectView(View):

    def get(self,request):
        if request.GET.get('id', ''):
            subject = Subject.objects.get(pk=request.GET.get('id'))
            return JsonResponse({
                'id': subject.id,
                'teacher_id' : subject.teacher_id,

            })

        subjects = Subject.objects.raw('select subject.id,subject.name,subject.teacher_id,teacher.name as teacher_name from subject join teacher on subject.teacher_id = teacher.id;')
        return render(request, 'basic/user_manager/sys_subject.html', locals())
    def post(self,request):
        print(request.POST)
        id = request.POST.get('id', None)  # 注意： form表单页面不建议使用id 字段名
        name = request.POST.get('name')
        teacher_id = request.POST.get('teacher_id')
        # 验证是否为空(建议:页面上验证是否为空)

        if id:
            # 更新
            subject = Subject.objects.get(pk=id)
            subject.name = name
            subject.teacher_id = teacher_id
            subject.save()
        else:
            Subject.objects.create(name=name, teacher_id=teacher_id)

        return redirect('/sys_subject/')
    def delete(self,request):
        subject_id = request.GET.get('id')
        subject = Subject.objects.get(pk=subject_id)
        subject.delete()

        return JsonResponse({
            'status': 0,
            'msg': '删除成功!'
        })
class ScoreView(View):

    def get(self,request):
        if request.GET.get('student_id', ''):
            student_id = request.GET.get('student_id')
            scores = Score.objects.raw('select score.id,score.student_id,students.name as student_name,score.subject_id,subject.name as subject_name from score  join students on score.student_id = students.id join subject on score.subject_id = subject.id where students.student_id = %s' % student_id)
            return render(request, 'basic/user_manager/sys_score.html', locals())

        scores = Score.objects.raw('select score.id,score.student_id,students.name as student_name,score.subject_id,subject.name as subject_name from score  join students on score.student_id = students.id join subject on score.subject_id = subject.id;')
        return render(request, 'basic/user_manager/sys_score.html', locals())
    def post(self,request):
        print(request.POST)
        id = request.POST.get('id', None)  # 注意： form表单页面不建议使用id 字段名
        student_id = request.POST.get('student_id')
        subject_id = request.POST.get('subject_id')
        value = request.POST.get('value')
        # 验证是否为空(建议:页面上验证是否为空)

        if id:
            # 更新
            score = Score.objects.get(pk=id)
            score.subject_id = subject_id
            score.student_id = student_id
            score.value = value
            score.save()
        else:
            Score.objects.create(student_id=student_id,subject_id=subject_id,value=value)

        return redirect('/sys_score/')
    def delete(self,request):
        score_id = request.GET.get('id')
        score = Score.objects.get(pk=score_id)
        score.delete()

        return JsonResponse({
            'status': 0,
            'msg': '删除成功!'
        })


class TeacherAddScoreView(View):

    def get(self,request):
        login_user = request.session.get('login_user')
        user_id = login_user['id']
        if request.GET.get('student_id', ''):
            student_id = request.GET.get('student_id')
            scores = Score.objects.raw(
                'select score.id,score.student_id,students.name as student_name,score.subject_id,subject.name as subject_name from score  join students on score.student_id = students.id join subject on score.subject_id = subject.id where students.student_id = %s' % student_id)
            return render(request, 'basic/user_teacher/teacher_add_score.html', locals())

        scores = Score.objects.raw("select score.id,score.student_id,students.name as student_name,score.subject_id,subject.name as subject_name from score  join students on score.student_id = students.id join subject on score.subject_id = subject.id where subject_id in (select id from subject where teacher_id = %s );" % user_id)
        return render(request, 'basic/user_teacher/teacher_add_score.html', locals())
    def post(self,request):
        print(request.POST)
        id = request.POST.get('id', None)  # 注意： form表单页面不建议使用id 字段名
        student_id = request.POST.get('student_id')
        subject_id = request.POST.get('subject_id')
        value = request.POST.get('value')
        # 验证是否为空(建议:页面上验证是否为空)

        if id:
            # 更新
            score = Score.objects.get(pk=id)
            score.subject_id = subject_id
            score.student_id = student_id
            score.value = value
            score.save()
        else:
            Score.objects.create(student_id=student_id,subject_id=subject_id,value=value)

        return redirect('/teacher_add_score/')
    def delete(self,request):
        score_id = request.GET.get('id')
        score = Score.objects.get(pk=score_id)
        score.delete()

        return JsonResponse({
            'status': 0,
            'msg': '删除成功!'
        })

class StudentScoreView(View):

    def get(self,request):
        if request.GET.get('id', ''):
            score = Score.objects.get(pk=request.GET.get('id'))
            return JsonResponse({
                'id': score.id,
                'student_id': score.student_id,
                'subject_id': score.subject_id,
                'value': score.value

            })
        login_user = request.session.get('login_user')
        user_id = login_user['id']
        scores = Score.objects.raw("select score.id,score.student_id,students.name as student_name,score.subject_id,subject.name as subject_name from score  join students on score.student_id = students.id join subject on score.subject_id = subject.id where score.student_id = %s;" % user_id)
        return render(request, 'basic/user_student/student_score.html', locals())

class StudentClassView(View):

    def get(self, request):
        if request.GET.get('id', ''):
            student_class = StudentClass.objects.get(pk=request.GET.get('id'))
            return JsonResponse({
                'id': student_class.id,
                'name': student_class.name


            })
        student_classes = StudentClass.objects.all()
        return render(request, 'basic/user_manager/sys_student_class.html', locals())

    def post(self, request):
        print(request.POST)
        id = request.POST.get('id', None)  # 注意： form表单页面不建议使用id 字段名
        name = request.POST.get('name')

        # 验证是否为空(建议:页面上验证是否为空)

        if id:
            # 更新
            student_class = StudentClass.objects.get(pk=id)
            student_class.name = name


            student_class.save()
        else:
            StudentClass.objects.create(name=name, )

        return redirect('/student_class/')

    def delete(self, request):
        student_class_id = request.GET.get('id')
        student_class = StudentClass.objects.get(pk=student_class_id)
        student_class.delete()

        return JsonResponse({
            'status': 0,
            'msg': '删除成功!'
        })

class Me(View):

    def get(self,request):
        login_user = request.session.get('login_user')
        user_id = login_user['id']
        students = Students.objects.raw(
            'select students.id,students.name,students.sex,student_class.name as class_name,students.auth_string,students.phone,students.email from students  join student_class on students.class_id=student_class.id  where students.id = %s' % user_id)
        return render(request, 'basic/user_student/me.html', locals())
    def post(self,request):
        print(request.POST)
        login_user = request.session.get('login_user')
        user_id = login_user['id']

        phone = request.POST.get('phone')
        email = request.POST.get('email')
        # 验证是否为空(建议:页面上验证是否为空)


        # 更新
        student = Students.objects.get(pk=user_id)
        student.phone = phone
        student.email = email
        student.save()
        return redirect('/me/')