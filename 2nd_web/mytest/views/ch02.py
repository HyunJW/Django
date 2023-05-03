from django.shortcuts import render, redirect
from mytest.models import Salary

def age(request):
    try:
        name = request.POST['name']
        year = request.POST['year']
    except:
        return render(request, 'ch02/age.html')
    age = 2023 - int(year) + 1
    return render(request, 'ch02/age_result.html',
                  {'name': name, 'year': year, 'age': age})

def mysum(request):
    try:
        num = int(request.POST['num'])
    except:
        return render(request, 'ch02/mysum.html')
    result = sum(range(1, num + 1))
    sum1 = 0 # 짝수 합계
    sum2 = 0 # 홀수 합계
    for i in range(1, num + 1):
        if i % 2 == 0:
            sum1 += i
        else:
            sum2 += i
    return render(request, 'ch02/mysum_result.html',
                  {'num': num, 'result': result,
                   'sum1': sum1, 'sum2': sum2})

def salary(request):
    try:
        name = request.POST['name']
        sal = int(request.POST['sal'])
        bonus = int(request.POST['bonus'])
    except:
        return render(request, 'ch02/salary.html')
    total = sal * 12 + bonus
    tax = total * 5 / 100
    money = total - tax

    Sal = Salary(name=name, sal=sal, bonus=bonus, total=total,
                 tax=tax, money=money)
    Sal.save()
    return render(request, 'ch02/salary_result.html',
                  {'name': name, 'sal': sal, 'bonus':bonus,
                   'total': total, 'tax': tax, 'money': money})

def salary_list(request):
    items = Salary.objects.order_by('id')
    return render(request, 'ch02/salary_list.html', {'items': items})

def salary_detail(request):
    id = request.GET['id']
    item = Salary.objects.get(id=id)
    return render(request, 'ch02/salary_detail.html', {'item': item})

def salary_update(request):
    id = request.POST['id']
    sal = int(request.POST['sal'])
    bonus = int(request.POST['bonus'])
    total = sal * 12 + bonus
    tax = total * 5 / 100
    money = total - tax

    item = Salary(id=id, name=request.POST['name'], sal=sal, bonus=bonus,
                  total=total, tax=tax, money=money)
    item.save()
    return redirect('/salary_list')

def salary_delete(request):
    Salary.objects.get(id=request.POST['id']).delete()
    return redirect('/salary_list')

def radio(request):
    try:
        name = request.POST['name']
        gender = request.POST['gender']
    except:
        return render(request, 'ch02/radio.html')
    if gender == 'male':
        gender = '남성'
    elif gender == 'female':
        gender = '여성'
    return render(request, 'ch02/radio_result.html',
                  {'name': name, 'gender': gender})

def checkbox(request):
    # 리스트로 값을 받아서 저장
    fruits = request.POST.getlist('fruits')
    if len(fruits) == 0:
        return render(request, 'ch02/checkbox.html')
    return render(request, 'ch02/checkbox_result.html',
                  {'fruits': fruits})

def button(request):
    try:
        price = request.POST['price']
        amount = request.POST['amount']
    except:
        return render(request, 'ch02/button.html')
    money = int(price) * int(amount)
    return render(request, 'ch02/button_result.html',
                  {'price': price, 'amount': amount, 'money': money})

def textarea(request):
    try:
        opinion = request.POST['opinion']
    except:
        return render(request, 'ch02/textarea.html')
    # textarea에 작성된 태그들를 막기 위한 처리
    opinion = opinion.replace('<', '&lt;')
    opinion = opinion.replace('>', '&gt;')
    # 줄바꿈 처리
    opinion = opinion.replace('\n', '<br>')
    # 중복된 띄어쓰기 처리
    opinion = opinion.replace('  ', '&nbsp;&nbsp;')
    return render(request, 'ch02/textarea_result.html',
                  {'opinion': opinion})

def select(request):
    if request.method == 'GET':
        return render(request, 'ch02/select.html')
    elif request.method == 'POST':
        # car = request.POST['car'] # 값이 1개일 때
        car = request.POST.getlist('car')  # 값이 2개 이상일 때
    return render(request, 'ch02/select_result.html',
                  {'car': car})

def select2(request):
    try:
        name = request.POST['name']
        color = request.POST['color']
    except:
        return render(request, 'ch02/select2.html')
    if color == 'blue':
        color = '파랑'
        bgcolor = 'blue'
    elif color == 'green':
        color = '초록'
        bgcolor = 'green'
    elif color == 'red':
        color = '빨강'
        bgcolor = 'red'
    return render(request, 'ch02/select2_result.html',
                  {'name': name, 'color': color, 'bgcolor': bgcolor})

def point(request):
    try:
        name = request.POST['name']
        kor = request.POST['kor']
        eng = request.POST['eng']
        mat = request.POST['mat']
    except:
        return render(request, 'ch02/point.html')
    total = float(kor) + float(eng) + float(mat)
    average = f'{total / 3:.2f}'
    return render(request, 'ch02/point_result.html',
                  {'name': name, 'kor': kor, 'eng': eng, 'mat': mat,
                   'total': total, 'average': average})

def gugu(request):
    # dan = int(request.POST['dan'])
    return render(request, 'ch02/gugu.html')

def gugu_result(request):
    dan = int(request.POST['dan'])
    result = ''
    for i in range(1, 10):
        result += f'{dan} x {i} = {dan * i}<br>'
    return render(request, 'ch02/gugu_result.html',
                  {'result': result})

