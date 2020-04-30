"""student_score_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import path,include

from common import make_pwd
from mainAPP.models import *
from mainAPP.views import *

def to_index(request: HttpRequest):
    return render(request, 'index.html', locals())


def to_login(request: HttpRequest):#登陆
    if request.method == "POST":
        # 获取用户名和口令
        name = request.POST.get('username', '')
        pwd = request.POST.get('password', '')
        sysuser = request.POST.get('sysuser', '')
        if any((not name, not pwd, len(name) == 0, len(pwd) == 0)):
            error = '用户名或口令不能为空!'

        else:
            if sysuser == "student":
                ret = Students.objects.filter(student_id=name, auth_string=make_pwd(pwd))
            elif sysuser == "teacher":
                ret = Teachers.objects.filter(job_num=name, auth_string=make_pwd(pwd))
            else:
                ret = SysManager.objects.filter(name=name, auth_string=make_pwd(pwd))

            if ret.exists():
                login_user = ret.first()

                # 将登录的用户信息存在session中
                request.session['login_user'] = {
                    'id': login_user.id,
                    'name': login_user.name,
                    'sysuser':sysuser
                }
                return redirect('/')

            error = "用户名或口令错误!"

    return render(request, 'login.html', locals())

def to_logout(req: HttpRequest):#登出
    req.session.pop('login_user')
    return redirect('/login/')
def sys_manager(request: HttpRequest):#系统管理员管理密码验证
    if request.method == 'GET':
        return render(request,'basic/user_manager/sys_manager_1.html')
    if request.method == "POST":
        pwd = request.POST.get('password', '')

        if any(( not pwd, len(pwd) == 0)):
            error =  "密码不能为空!"
        else:
            if pwd == "102999":
                return redirect('/sys_manager_2/')

            error =  "密码输入错误"
        return render(request,'basic/user_manager/sys_manager_1.html',locals())
def manage_pwd(request: HttpRequest):#修改密码
    if request.method == 'GET':
        return render(request,'basic/user_manager/manage_pwd.html')
    if request.method == 'POST':
        pwd_old = request.POST.get('password_old','')
        pwd_new = request.POST.get('password_new','')
        if any((not pwd_new,not pwd_old, len(pwd_new) == 0,len(pwd_old) == 0)) :
            error = '密码不能为空'
        else:
            login_user = request.session.get('login_user')
            print(login_user,type(login_user))
            user_id = login_user['id']
            user_name = login_user['name']
            user_role = login_user['sysuser']
            print(user_name)
            if user_role == "student":
                ret = Students.objects.filter(name=user_name, auth_string=make_pwd(pwd_old))
                if ret.exists():
                    student = Students.objects.get(pk=user_id)
                    student.auth_string = make_pwd(pwd_new)
                    student.save()
                    return redirect('/')

                error = "旧密码错误"
            elif user_role == "teacher":
                ret = Teachers.objects.filter(name=user_name, auth_string=make_pwd(pwd_old))
                if ret.exists():
                    teacher = Teachers.objects.get(pk=user_id)
                    teacher.auth_string = make_pwd(pwd_new)
                    teacher.save()
                    return redirect('/')

                error = "旧密码错误"
            else:
                ret = SysManager.objects.filter(name=user_name, auth_string=make_pwd(pwd_old))
                if ret.exists():
                    manage = SysManager.objects.get(pk=user_id)
                    manage.auth_string = make_pwd(pwd_new)
                    manage.save()
                    return redirect('/')

                error = "旧密码错误"
        return render(request,'basic/user_manager/manage_pwd.html',locals())








urlpatterns = [
    path('login/', to_login),
    path('logout/', to_logout),
    path('', to_index),
    path('sys_manager/', sys_manager),
    path('sys_manager_2/',ManagerView.as_view()),
    path('sys_student/',StudentView.as_view()),
    path('sys_teacher/',TeacherView.as_view()),
    path('manage_pwd/',manage_pwd),
    path('sys_subject/',SubjectView.as_view()),
    path('sys_score/',ScoreView.as_view()),
    path('teacher_add_score/',TeacherAddScoreView.as_view()),
    path('student_score/',StudentScoreView.as_view()),
    path('student_class/',StudentClassView.as_view()),
    path('me/',Me.as_view())


]
