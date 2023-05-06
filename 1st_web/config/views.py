from django.shortcuts import render

def home(request): # request: 사용자의 요청사항 처리객체
    # 화면생성
    return render(request, 'index.html') # render(전달할데이터, 화면템플릿)