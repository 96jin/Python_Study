# 컬렉션

## 리스트

a = []      # 빈 리스트
b = [1, 2, 3]       # 정수로만 이루어진 리스트
c = ['a', 'b', 'c', 'd']        # 문자열로 이루어진 리스트
d = [1, 2, 'a', 'b', True]      # 여러 자료형으로 이루어진 리스트
e = [1, 2, ['a', 'b']]          # 이중 리스트

print(a)
print(b)
print(c)
print(d)
print(e)

# 리스트 인덱싱

print(b[1])
print(c[3])
print(d[0])
print(e[2])
print(e[-1])        # 맨 마지막을 뜻한다
print(e[2][0])      # 이중 리스트 안의 값을 출력하고자 할때

f = [1, 2, ['a','b',['안녕','하세요']]]      # 3중 리스트

print(f)
print(f[2])
print(f[2][2])
print(f[2][2][0])

=====================실행 결과=====================
[]
[1, 2, 3]
['a', 'b', 'c', 'd']
[1, 2, 'a', 'b', True]
[1, 2, ['a', 'b']]
2
d
1
['a', 'b']
['a', 'b']
a
[1, 2, ['a', 'b', ['안녕', '하세요']]]
['a', 'b', ['안녕', '하세요']]
['안녕', '하세요']
안녕

# 리스트 슬라이싱

a = [1, 2, 3, 4, 5]
print(a[0:2])
print(a[2:3])
print(a[:3])    # 처음부터 (0 생략가능)
print(a[2:])    # 끝까지 (끝번호 생략가능)

b = [1, 2, 3, ['b','c','d'], 4, 5]
print(b[2:5])
print(b[3][:2])     # b[3]에서 0번, 1번 인덱스 자료를 출력해라.

=====================실행 결과=====================

[1, 2]
[3]
[1, 2, 3]
[3, 4, 5]
[3, ['b', 'c', 'd'], 4]
['b', 'c']

# 리스트 연산자

list_a = [1, 2, 3]
list_b = [4, 5, 6]

print('list_a :', list_a)
print('list_b :', list_b)

print('list_a + list_b :', list_a + list_b) # 하나의 리스트로 합쳐진다.
print('list_a * 3 :', list_a * 3)   # 3번 반복 출력된다.


=====================실행 결과=====================

list_a : [1, 2, 3]
list_b : [4, 5, 6]
list_a + list_b : [1, 2, 3, 4, 5, 6]
list_a * 3 : [1, 2, 3, 1, 2, 3, 1, 2, 3]


# 리스트 요소 (값) 추가 : append, insert

list1 = [1, 2, 3]
print('list1 :', list1)

list1.append(4)     # append 함수는 리스트 맨 뒤에 값을 추가
print('list1 :', list1)

list1.append(100)
print('list1 :', list1)

list1.insert(0, 50) # 0번 자리에 50을 넣겠다.
print('list1 :', list1)

=====================실행 결과=====================

list1 : [1, 2, 3]
list1 : [1, 2, 3, 4]
list1 : [1, 2, 3, 4, 100]
list1 : [50, 1, 2, 3, 4, 100]



# 리스트 요소(값) 제거 (인덱스 번호로 삭제) : del, pop

list2 = [0, 1, 2, 3, 4, 5]
print('list2 :', list2)

del list2[1]    # 1번 인덱스 자료를 삭제
print('list2 :', list2)

list2.pop(2)    # 2번 인덱스 자료를 삭제
print('list2 :', list2)

print()

list3 = [0, 1, 2, 3, 4, 5, 6]
print('list3 :' , list3)

del list3[3:6]  # 슬라이싱 삭제는 del 함수만 가능
print('list3 :' , list3)


=====================실행 결과=====================

list2 : [0, 1, 2, 3, 4, 5]
list2 : [0, 2, 3, 4, 5]
list2 : [0, 2, 4, 5]

list3 : [0, 1, 2, 3, 4, 5, 6]
list3 : [0, 1, 2, 6]



# 튜플    -   읽기 전용 리스트 (값 수정 불가)

t1 = (1, 2, 3)
print('t1 :', t1)

t2 = 1, 2, 3    # 소괄호 생략 가능
print('t2 :', t2)

t3 = tuple([100, 3.14, 'hello'])
print('t3 :', t3)

t4 = (100)      # 튜플이 아닌 일반 변수로 인식
print('t4 :', t4)

t5 = (100,)     # 값이 하나일때는 쉼표를 붙여준다
print('t5 :', t5)

=====================실행 결과=====================

t1 : (1, 2, 3)
t2 : (1, 2, 3)
t3 : (100, 3.14, 'hello')
t4 : 100
t5 : (100,)



# 리스트와 튜플의 차이점

    리스트는 [], 튜플은 ()
    리스트는 요소의 추가, 수정, 삭제 가능
    튜플은 요소를  바꿀 수 없다

# 리스트와 튜플의 공통점

    연산 가능 (덧셈, 곱셈)
    인덱싱, 슬라이싱 가능



# 세트 (집합)

s1 = {1, 2, 3}
print('세트 s1 :', s1)

# 값을 1개 추가하기 (add)

s1.add(4)
print('세트 s1 :', s1)

# 값을 여러개 추가하기 (update)

s1.update([5, 6, 7])
print('세트 s1 :', s1)

# 특정값을 제거하기 (remove)

s1.remove(3)    # 값 3을 지워라
print('세트 s1 :', s1)

=====================실행 결과=====================

세트 s1 : {1, 2, 3}
세트 s1 : {1, 2, 3, 4}
세트 s1 : {1, 2, 3, 4, 5, 6, 7}
세트 s1 : {1, 2, 4, 5, 6, 7}


# 딕셔너리

dic = {'name' : '홍길동', 'birthday' : '1212'}
print('딕셔너리 dic :', dic)

# 특정값을 출력할 때

print(dic['name'])

# 딕셔너리 값을 수정 할 때

dic['name'] = '라이언'
print('딕셔너리 dic :', dic)

# 딕셔너리 쌍을 추가 할 때

dic['address'] = '대구'       # 해당하는 키가 없으면 추가됨
print('딕셔너리 dic :', dic)

# 딕셔너리 쌍을 삭제하기

del dic['address']      # address에 해당하는 키와 값을 삭제
print('딕셔너리 dic :', dic)

# key 리스트 만들기

print(dic.keys())       # key 부분만 따로 모은것

# 값(value) 리스트 만들기

print(dic.values())     # 값 부분만 따로 모은것

# items 함수를 이용해서 쌍을 얻기

print(dic.items())      # 쌍이 튜플 형식으로 묶인다

# 키와 값을 모두 지우기

dic.clear()
print('딕셔너리 dic :', dic)

=====================실행 결과=====================

딕셔너리 dic : {'name': '홍길동', 'birthday': '1212'}
홍길동
딕셔너리 dic : {'name': '라이언', 'birthday': '1212'}
딕셔너리 dic : {'name': '라이언', 'birthday': '1212', 'address': '대구'}
딕셔너리 dic : {'name': '라이언', 'birthday': '1212'}
dict_keys(['name', 'birthday'])
dict_values(['라이언', '1212'])
dict_items([('name', '라이언'), ('birthday', '1212')])
딕셔너리 dic : {}


# 표준 출력

# 이스케이프 문자

    프로그래밍 할 때 사용할 수 있도록 미리 정의해둔 문자 조합
    출력물을 보기 좋게 정렬하는 용도로 사용



# 55p

print('재미있는', '파이썬')
print('Python', 'Java', 'C', sep=',')
print()     # 빈 줄

print('영화 타이타닉')
print('평점', end=':')
print('5점')

fos = open('sample.py', mode='wt')
print('print("Hello World")', file=fos)     # 파일에 출력
fos.close()

=====================실행 결과=====================

재미있는 파이썬
Python,Java,C

영화 타이타닉
평점:5점



# 형식을 갖춘 문자열 (문자열 포맷팅)

# % 연산자 (기본 포맷팅)

#58p

name = 'kai'
print('내 이름은 %s 입니다' %name)     # 문자열

height = 120.5                      
print('내 키는 %.2f cm 입니다' %height)   # 실수

weight = 23.55                  
print('내 몸무게는 %.1f kg입니다' %weight)  # 소수 첫째자리까지 반올림

year, month, day = 2014, 8, 25
print('내 생일은 %d년 %d월 %d일 입니다' %(year,month,day))    # 10진수 정수

=====================실행 결과=====================

내 이름은 kai 입니다
내 키는 120.50 cm 입니다
내 몸무게는 23.6 kg입니다
내 생일은 2014년 8월 25일 입니다










      
