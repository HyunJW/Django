from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as dlogin, logout as dlogout
from member.models import UserForm, LoginForm

#시작 페이지
def home(request):
    # 로그인 하지 않은 상태
    if not request.user.is_authenticated:
        data = {"username": request.user,
                "is_authenticated": request.user.is_authenticated}
    # 로그인 한 상태
    else:
        data = {"last_login": request.user.last_login,
                "username": request.user.username,
                "password": request.user.password,
                "is_authenticated": request.user.is_authenticated}
    return render(request, 'member/index.html', {'data': data})

#회원가입 처리
def join(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        # 입력값에 문제가 없으면
        if form.is_valid():
            # 새로운 사용자 생성
            new_user = User.objects.create_user(**form.cleaned_data)

            # 로그인 처리
            dlogin(request, new_user)

            # 시작페이지로 이동
            return redirect("/member")
        else:
            return render(request, 'member/index.html',
                          {'msg': '회원가입 실패... 다시 시도해 보세요.'})
    else: # post방식이 아닌 경우 회원가입 페이지로 이동
        form = UserForm()
        return render(request, 'member/join.html', {'form': form})

def login_check(request):
    if request.method == "POST":
        name = request.POST['username']
        pwd = request.POST['password']
        # 인증
        user = authenticate(username=name, password=pwd)

        # 로그인 성공
        if user is not None:
            dlogin(request, user)
            request.session['userid'] = name
            return redirect('/member')

        # 로그인 실패
        else:
            return render(request, 'member/index.html',
                          {'msg': '로그인 실패... 다시 시도해 보세요.'})
    else: # get 방식인 경우 - 로그인 페이지로 이동
        form = LoginForm()
        return render(request, 'member/login.html', {'form': form})

def logout(request):
    dlogout(request)
    return redirect('/member')