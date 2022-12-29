# 사칙연산
a = 10
b = 20
c = a + b * 10 - 5 / 5

print(c)
#👉 실행 결과 :
209.0
================
x = 20
y = 4

x = y % x
print(x)

y -= x * 2
print(x, y)

#✍ 문제 풀이 (실행 결과)
x = 4 % 20 = 4    # 4를 20으로 나누면 몫은 0, 나머지는 4
y = y - (x * 2)
  = 4 - (4 * 2)   # 위에서 x = 4가 되었으므로, 20이 아닌 4 대입
  = 4 - 8
  = -4

정답 : 4, 4, -4

===========================

# 나머지 연산, 소수점 절삭 연산
x = 10 % 3 # 10을 3으로 나눈 나머지
print(x)

y = 7//3 # 7을 3으로 나눈 다음 소수점 이하를 절삭
print(y)
#👉 실행 결과 :
1
2

==================
# 거듭제곱 연산
x = 2**3 # 2의 3승의 값 (2*2*2)
print(x)

y = 10**4 # 10의 4제곱 (10*10*10*10)
print(y)
#👉 실행 결과 :
8
10000
===================
# str2_ex1)
hello = '안녕' * 5

print(hello)

# str2_ex2)
name = '홍길동'
greet = name + '님 안녕하세요!'

print(greet)
#👉 실행 결과 :
#홍길동님 안녕하세요!

========================
# str_ex4)
eng = 80
result = '영어 점수 : ' + str(eng) + '점'

print(result)
#👉 실행 결과 :
#영어 점수 : 80점
==================
# ex1)
name = '김철수'
a = '나는 %s입니다.' % name
print(a)

# ex2)
age = 20
b = '나이는 %d살 입니다.' % age
print(b)

# ex3)
year = 2021
month = 10
day = 3

c = '%d-%02d-%02d' % (year, month, day)
print(c)

# ex4)
height = 172.5
d = '키는 %.2f입니다.' % height
print(d)

#👉 실행 결과 :
#나는 김철수입니다.
#나이는 20살 입니다.
#2021-10-03
#키는 172.50입니다.

==============================
name = '황예린'
age = 18
eyesight = 1.2

a = '이름 : {}'.format(name)
b = '나이 : {}세'.format(age)
c = '시력 : {}'.format(eyesight)

print(a)
print(b)
print(c)
👉 실행 결과 :
이름 : 황예린
나이 : 18세
시력 : 1.2

# bool_ex)
a = True
b = False
print(a)
print(b)

c = 10 > 20 # 10이 20보다 큰가요?
print(c) # 위 질문의 결과 출력

print(type(a)) # 데이터 형 출력
👉 실행 결과 :
True
False
False # 10은 20보다 크지 않으므로 거짓이다.
<class 'bool'>

============================

x = int(input('숫자를 입력하세요 : '))

if x > 0:
    print('양수!')          # 참(True)인 경우
    
else:
    print('0 또는 음수!')   # 거짓(False)인 경우
#👉 실행 결과1. 23을 입력했을 경우
#숫자를 입력하세요 : 23
#양수!
======================
# 비교연산자를 사용한 짝수/홀수 판별
num = int(input('숫자를 입력하세요 : '))

if num % 2 == 0:       # num/2의 나머지가 0 이면(참),
    print('짝수이다.')  # 참이면 이 문장을 실행

else:                  # 위의 if문이 False(거짓)이면,
    print('홀수이다.')  # 거짓이면 이 문장을 실행

#👉 실행 결과1. 짝수가 입력되었을 경우
#숫자를 입력하세요 : 24
#짝수이다.
#👉 실행 결과2. 홀수가 입력되었을 경우
#숫자를 입력하세요 : 35
#홀수이다.
=================================

# 자격증 시험 합격/불합격 판정
score1 = int(input('필기성적을 입력하세요 : '))
score2 = int(input('실기성적을 입력하세요 : '))

if score1 >= 80 and score2 >= 80:   # 조건 2가지 모두 만족해야 참(True)
    print('합격!')                  # 참(True)인 경우 출력
    
else:
    print('불합격!')                # 거짓(False)인 경우 출력
#👉 실행 결과1 :
#필기성적을 입력하세요 : 90
#실기성적을 입력하세요 : 80
#합격!

==========================

# 홈페이지 관리자 판별
id = input('아이디를 입력하세요 : '))
level = int(input('회원 레벨을 입력하세요 : '))

if id == 'admin' or level == 1:   # 조건 2가지 중 1가지만 만족해도 참(True)
    print('관리자이다.')           # 참(True)인 경우 출력

else:
    print('관리자가 아니다.')      # 거짓(False)인 경우 출력
#👉 실행 결과1 :
#아이디를 입력하세요 : admin
#회원 레벨을 입력하세요 : 1
#관리자이다.

===============================
# if~ 구문을 이용하여 입장료 계산하기
age = int(input('나이를 입력하세요 : '))
pay = '3000원'

if age >= 65 or age < 7:
    pay = '무료'
    
print('입장료 : %s' % pay)
#👉 실행 결과1. 나이가 65이상 또는 7 미만인 경우
#나이를 입력하세요 : 67
#입장료 : 무료
=========================
answer = '12345'
password = input('비밀번호를 입력하세요 : ')

if password == answer:
    print('비밀번호 OK!')

else:
    print('비밀번호 Not Ok!')
#👉 실행 결과 :
#비밀번호를 입력하세요 : 34566
#비밀번호 Not Ok!
================================
# 점수에 따른 등급을 나누는 예제
score = int(input('점수를 입력하세요 : '))

if score >= 90:
    grade = 'A'

elif score >= 80:
    grade = 'B'

elif score >= 70:
    grade = 'C'

elif score >= 60:
    grade = 'D'

else:
    grade = 'F'

print('성적 : %d점' % score)
print('등급 : %s' % grade)

#👉 실행 결과 :
#점수를 입력하세요 : 85
#성적 : 85점
#등급 : B

===========================================
age = int(input('나이를 입력하세요 :'))

if age < 11:  # 10세 이하
    price = '1000원'

elif age >= 65:  # 65세 이상
    price = '0원'

else:  # 나머지 (기본)
    price = '2000원'
    
print('입장료는', price, '입니다.')

#👉 실행 결과
#나이를 입력하세요 : 6
#입장료는 1000원 입니다.
============================================
eng = int(input('영어시험 점수를 입력하세요 :'))
math = int(input('수학시험 점수를 입력하세요 :'))

if eng >=80 and math >= 80:
    print('합격')

elif eng < 80 and math < 80:
    print('불합격')

elif eng >= 80 or math >= 80:
    print('재시험 기회제공')

#👉 실행 결과
#영어시험 점수를 입력하세요 : 85
#수학시험 점수를 입력하세요 : 75
#재시험 기회제공
==========================================

# ex3. 1~10까지 정수의 합계 구하기
sum = 0

for i in range(1, 11):  # 1부터 10까지 (마지막 숫자는 포함 X)
    sum += i
    print('i의 값 : %d, 합계 : %d' % (i, sum))

======================================================

# Step1. 2단 구구단표 만들기
a = 2

for b in range(1, 10):
    c = a * b
    print('%d x %d = %d' % (a, b, c))

=========================================

#Step2. 전체 구구단표 만들기
print('-' * 50) # 단마다 구분하기 위해서(테두리 생성)

for a in range(2, 10):  # --------- (1)
    for b in range(1, 10):  # ----- (2)
        c = a * b
        print('%d x %d = %d' % (a, b, c))
        
    print('-' * 50) # 단마다 구분하기 위해서(테두리 생성)

======================================================

buy = int(input('물건 구매가를 입력하세요 : '))

if buy >= 10000 and buy < 50000 :
    rate = 5

elif buy >= 50000 and buy < 300000 :
    rate = 7.5

elif buy >= 300000 :
    rate = 10

else:
    rate = 0

discount = buy * rate / 100
pay = buy - discount

print('구매가 : %.0f원' % buy)
print('할인율 : %.1f%%' % rate)      # %가 2개여야 할인율 단위(%)가 제대로 출력됨
print('할인 금액 : %.0f원' % discount)
print('지불 금액 : %.0f원' % pay)

==================================
for i in range(1, 1001):
    print(i)
    
    if i == 10:
        break
==============================

# ex1. 리스트 생성과 추출
# 리스트 생성
fruits = ['사과', '오렌지', '딸기', '포도', '감', '키위', '멜론', '수박']
list1 = [5, 10.2, '탁구', True, [4, 5, 6]] # 리스트는 다양한 데이터 형을 섞어서도 가능
numbers = list(range(1, 10, 2))

print(fruits)
print(list1)
print(numbers)

# 리스트 추출
print()
print(fruits[0])     # 인덱스는 0부터 시작하므로 fruits의 가장 첫 번째 요소 출력
print(fruits[1:4])   # 인덱스 1~3의 요소 추출 (마지막 숫자(4)는 포함 X)
print(fruits[2:])    # 인덱스 2부터 끝까지 다 추출
print(fruits[-1])    # 뒤에서 첫번째 요소 추출 (마지막 요소 추출)
print(fruits[-4:-2]) # 끝에서 4번째 요소부터 끝에서 3번째 요소까지 출력
print(fruits[-3:])   # 끝에서 3번째 요소부터 다 추출

==================================

# ex2. 리스트 요소 추가
a = ['red', 'green', 'blue'] # 리스트 생성
a.append('yellow')           # 리스트 a의 끝에 'yellow' 추가
print(a)

a.insert(1, 'black')         # 리스트 a의 인덱스 1의 요소에 'black' 추가
print(a)

b = ['purple', 'white']      # 리스트 생성
a.extend(b)                  # 리스트a와 b를 병합 (extend : 두 리스트 병합)
print(a)

c = a + b                    # extend와 같은 기능
print(c)                     # 위에서 병합된 a에 b를 또 추가

======================================

# ex3. 리스트 요소 삭제
a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100] # 리스트 생성
x = a.index(30) # 리스트 a의 요소들 중 30의 인덱스
print(x)

a.pop(x) # 위에서 x가 2였으므로, 2번째 인덱스 요소(30) 삭제 (del a[x]와 동일)
print(a)

a.remove(90) # 90의 값을 가진 요소 삭제
print(a)

a.clear() # 리스트 a의 모든 요소 삭제
print(a)

==================================

# ex4. 리스트 요소 카운트
list1 = ['a', 'bb', 'c', 'd', 'aaa', 'c', 'ddd', 'aaa', 'b', 'cc', 'd', 'aaa']
length = list1.count('aaa') # list1의 요소 중 'aaa'의 값을 가지는 요소의 개수 세기

print(length)
======================

# ex5. 리스트 정렬
list2 = [-7, 1, 5, 8, 3, 9, 11, 13]
list2.sort() # 오름차순 정렬
print(list2)

list2.sort(reverse=True) # 내림차순 정렬
print(list2)
==========================

# ex2. 리스트로 합계와 평균 구하기
scores = [88, 75, 90, 95, 77, 69, 80, 92]

sum = 0
for score in scores:
    sum += score  # 총점 구하기

avg = sum/8       # 평균구하기 (총점/과목수)

print('총점 : %d, 평균 : %.2f' % (sum, avg))
=============================
# ex2. 딕셔너리의 기본 구조
members = {'name': '안지영', 'age': 30, 'email': 'jiyoung@korea.com'} # 딕셔너리 생성

print(members)          # 딕셔너리 추출
print(members['name'])  # 키 'name'에 대응되는 값 출력
print(members['age'])   # 키 'age'에 대응되는 값 출력

print('길이' : %d' % len(members))
================================

ords = {'사과': 'apple', '컴퓨터': 'computer', '학교': 'school', '책상': 'desk', '의자': 'chair'}

for key in words:
    in_word = input('%s에 해당되는 영어 단어를 입력해주세요: ' % key)
    
    if in_world == words[key]:
        print('정답입니다!')
        
    else:
        print('틀렸습니다!')
=================================
