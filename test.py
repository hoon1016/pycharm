# print('Hello world1!!')
#print('Hello worl2d!!')

# a = 10
#
# if a == 10:
#     print('10')

# print(1+1)
# print(2-1)
# print(2*5)
# print(5/2)
# print(5//2) #몫 구하기
# print(5%2)   #나머지 구하기
# print(2**3)
#
# print(int(3.3))
# print(int(5/2))
# print(5//2)

# print(type(10))
# print(type('10'))
# print(divmod(5,2))
# print(float(3))

# print(2+3)
#
# x = 2 #대입연산자
# print(x)
# print(type(x))
#
# x = 1
# y = 2
# z = 3
# x,y,z = 1,2,3
# print(x)
# print(y)
# print(z)
#
# x=y=z=10
# print(x,y,z)

# del x
# print(x)

# x = None
# print(x)
#
# a = 10
# b = 20
# c = a + b
# print(c)
#
# a = 30
# c = a + b
# print(c)
#
# name = '링크' #변수의 초기화
# print(name)
# name = 20
# print(name)

# x = input('정수를 입력하세요:')
# print(x)


# a = int(input('정수를 입력하세요:'))
# b = int(input('정수를 입력하세요:'))
# print(a+b)

# a,b = input('정수를 두개를 입력하세요').split(',')
# print(int(a)+int(b))

# x = 10
# y = 20
# print(x,y)
#
# x,y = y,x  #Swap
# print(x,y)

# a = 10
# print(a)
# a += 20 # a = a + 20
# print(a)
# a,b = map(int,input('숫자두개 입력;').split())
# print(a+b)

# a,b,c,d = map(int,input().split())
# s = (a+b+c+d) /4
# print(int(s))
# a = 5
# b = 3
# print(a ** b)
# print('Hello world!')
# a,b = map(int,input().split())
# avg = (a**b)
# print(int(avg))
# a = 10
# b = 30
# c = None
# print(a,b,c
#
# a = 100
# if a == 100:
#     print('100')
# a = 10
# b = 20
# d = 30
# e = 142
# print(a+b+d+e)
# a,b map(int,input().split())
# avg = (a**b)
# print(avg)
# print(10)
# print(1,2,3)
# print(2,3,2)
# print(3,2,3,sep=',')
# print(2,3,sep='x')
# print(3,2,3,sep='/n')
# print('1/n2/n3')
# print(1,end='')
# print(2,end='')
# print(3)

# 논리값
# True / False

# 비교연산자
# >,<,>=,<=,==,!=
# print(3>5)
# print(10 == 10)
# print(10 != 10)
# print(1 == 1.0)
# print(1 is 1.0) 타입까지 비교한다.

#논리연산자  : 두개이상의 조건을 구성할때 사용한다
#and, or, not
#and : 모든식이 True 일때 결과는 True
#T and F   F
#T and T   T
#F and T   F
#F amd F   F
#or : 모든식이 False 일때 결과는 True
#T or F     T
#T or T     T
#F or T     T
#F or F     F
#not
#not T     F
#not F     T

# print(True and True)
# print(False or False)
# print((not True)

# x = 10
# y = 20
# z = 30
# x == 10 and y == 20
#
# print(x == 10 and y == 20)
# print(x == 10 and y == 30)
# print(x == 10 and y == 20 and z == 30)
#
# print(x == 10 or y == 20)
# print(x == 10 or y == 30)
# print(x == 10 or y == 200 or z == 300)
# print(x == 100 or y == 200)
#
# print(not x == 10)
#
# #단락평가
# print(False and True)
# print(True and 'python')
# print('python' or True)
# print(0 and 0)
# print(0 or False)

# 숫자는 0을 제외하고 모두 True 이다
#문자는 ''를 제외하고 모두 True이다다

# k,e,m,s = map(int,input().split())
# print(k >= 90 and e > 80 and m >85 and s >=80)

#문자(String)
# str = 'Hello world' #'' or ""
# str1 = '''Hello world
#             안녕하세요
#             화이팅 입니다'''
# print(str1)
# str2 = "Python isn't difficult"
# print(str2)
# str3 = 'Python isn\'t difficult'
# print(str3)

#리스트 , 튜플
#[] , ()

# a = [1,2,3,4,5]
# print(a)
#
# a = []
# print(a)
#
# a = list()
# print(a)
#
# print(range(10))
#
# b = list(range(10))
# print(b)
#
# c = list(range(5,12))
# print(c)
# d = list(range(-4,10,2))
# print(d)
# e = list(range(12,24))
# print(e)

#튜플

# a = (1,2,3,4,5)
# print(a)
# b = 1,2,3,4,5
# print(b)
# c = ('james' ,1,2,3,True)
# print(c)
# d = (43,)
# print(d)
# #tuple()
# e = tuple(range(10))
# print(e)
# f = tuple(range(-4,10,2))
# print(f)
#
# a = [1,2,3,4,5]
# print(tuple(a))
#
# b = (1,2,3,4,5)
# print(b)
# print(list(b))
#
# print(list('Hello'))
# print(tuple('Hello'))
#
# a,b,c = [1,2,3]
# print(a,b,c)
#
# a,b,c = (1,2,3)
# print(a,b,c)
#
# y = [1,2,3]
# a,b,c = y
# print(a,b,c)

# x = input().split()
# print(x)

#리스트, 튜플, range,문자열
#공통가능
# a = [0,10,20,30,40,50,60,70,80,90,]
# print(30 in a)
# print(30 not in a)
#
# # + 연산가능(연결)
# a = [1,2,3,4,5]
# b = [6,7,8,9,10]
#
# print(a+b)
#
# print(list(range(10))) + list(range(11,20)
# tuple(range(10)) + list(range(11,20))
#
# print('hello ' + 'world! !')
# print('hello' + str(10))
#
# x = [1,2,3,4,5] * 3
# print(x)
#
# #시퀸스객체의 크기
# x = [1,2,3,4,5,6,7,8,]
# print(len(x))
# h = 'hello world!!'
# print(len(h))
#
# #인덱스값
# x = [1,2,3,4,5,6,7,8]
# print(x[0])
# print(x[5])
# print(x[-1]) #x[7]
# print(x[len(x)-1])
# h = 'hello world!!'
# print(h[0])
# print(h[6])
# print(h[-7])
# # print(h[23])
#
#
# print('=================')

# a = [0,0,0,0,0]
# print(a)
# a[0] = 10
# a[1] = 20
# a[2] = 30
# a[3] = 40
# a[4] = 50
# print(a)
#
# del a[2]
# print(a)
#
# b = (10,20,30,40,50)
# print(b)
# b[0] = 100 #수정불가
# print(b)
# del b[2] #삭제불가
# print(b)

 #슬라이스
# a = [1,2,3,4,5,6,7,8,9]
# print(a[0:4])
# print(a[1:1])
# print(a[1:2])
# print(a[4:7])
# print(a[2:8:3])
# print(a[:7])
# print(a[7:])
# print(a[:]) #전체값 a[::]
# print(a[:7:2])
# print(a[7::2])
# print(a[::2])
# a = [10,20,30,40,50,60,70,80,90]
# print(a[5:1:-1])

# h = 'Hello world!'
# print(h[::2])
# print(h[1::2])

# a = [10,20,30,40,50,60,70,80,90]
# a[2:5] = ['a','b','c']
# print(a)
#
# a = [10,20,30,40,50,60,70,80,90]
# a[2:5] = ['a','b','c','d','e']
# print(a)
#
# a = [10,20,30,40,50,60,70,80,90]
# a[2:8:2] = ['a','b','c']
# print(a)
#
# a = [10,20,30,40,50,60,70,80,90]
# del a[2:8:2]
# print(a)

#딕셔너리
# k:v
# lux = {'health':490,'mana':334,'melee':550,'armor':18.72}
# print(lux)
# lux = {100:'asdf',False:0,3.4:[2,3]}
#
# x = {}
# print(x)
# x = dict()
# print(x)

#딕셔너리명 = {키:값1,키:값2,.......}
#key값은 중복을 허용하지 않는다.
#value값은 중복을 허용한다.
# 딕셔너리명 = {}
# 딕셔너리명 = {key:value,key:value...}
# 딕셔너리명 = dict()
# 딕셔너리명 = dict(key=value,key=value) //key값이 문자인경우 '' 불가
# 딕셔너리명 = dict(zip([key,key],[value,value]))
# 딕셔너리명 = dict([(key,value),(key,value)])
# 딕셔너리명 = dict({key:value,key:value....})

# lux1 = dict(health=400,mama=334,melee=550,armor=18.72)
# print(lux1)
#
# lux2 = dict(zip(['health','mana','melee','armor'],[400,334,550,18.72]))
# print(lux2)
#
# lux3 = dict([('health',400),('mana',334),('melee',550),('armor',18.72)])
# print(lux3)
#
# lux4 = dict({'health':400,'mana':334,'melee':550,'armor':18.72})
# print(lux4)
#
# lux = {'health':400,'health':800,'mana':334,'melee':550,'armor':18.72}
# print(lux['health'])
# print(lux['health'] + lux['mana'])
#
# lux['health'] = 2021
# print(lux['health123'])
#
# lux['mana_regon'] = 3.25 #신규데이터로 추가
# print(lux)
# print(len(lux))

#조건문

# if 조건식(True/False):
#     실행문1
#     실행문2
#실행문3

# x = 10
# if x == 10:
#     print('x는 10입니다')
#
# if x == 10:
#     pass
#
# if x != 10:
#     print('x는 10입니다')
# print('무조건실행')

#중첩구조
# x = 15
# if x > 10:
#     if x == 15:
#         print('x는 15입니다')


# x = int(input())
# if x == 10:
#     print('x는 10입니다')

# x = 5
# if x == 10:
#     print('10입니다')
# else:
#     print('10이 아닙니다')

# if '0':
#     print("참")
# else:
#     print('거짓')

# x = 10
# y = 20
# if x == 10 and y == 20:
#     print('참')
# else:
#     print('거짓')
#
# z = 21
# if z > 0 and z < 100:
#     print("참")
# else:
#     print('거짓')
#
# z = 21
# if 0 < z < 100:  #z > 0 and z < 100

# x=20
# if x == 10:
#     print("10")
# elif x == 20:
#     print('20')
# elif x == 30:
#     print('30')
# else:
#     print("없다")
#
#
# if x == 10:
#     print("10")
# if x == 20:
#     print('20')
# if x == 30:
#     print('30')

# button = int(input())
#
# if button == 1:
#     print('콜라')
# elif button == 2:
#     print('사이다')
# elif button == 3:
#     print('환타')
# else:
#     print('잘못 입력했네요')

#반복문 for , while
# for 변수 in 값:
#     실행문
# for i in range(10):
#     print('Hello, world!')
#
# for i in range(10):
#     print('Hello, world!',i)

# for i in range(0, 10, 2):  # 0부터 8까지 2씩 증가
#     print('Hello, world!',i)
# for i in range(10, 0, -1): # 10에서 1까지 1씩 감소
    # print('Hello,world',i)
# for i in  reversed(range(11)):
#     print('Hello',i)

# for i in  range(10):
#     print(i,end=' ')

# cnt = int(input())
# for i in  range(cnt):
#     print(i,end=' ')
# a = [10,20,30,40,50]
# for i in  [10,20,30,40,50]: #for i in a: 두개 다 가능하다
#     print(i)

# for i in 'python': #for i in reversed('python'):
#     print(i)
# for i in 'python':
#     print(i,end=' ')

# while 조건식 (True/False):
#       실행문

# i = 0
# while i < 10:
#     print('Hello',i)
#     i += 1

# i = 0
# cnt = int(input())
# while i < cnt:
#     print('hello',i)
#     i += 1

#무한반복
# while True: 숫자나,문자
#     print('hello')

import random

#print(random.random())
# print(random.randint(1,6))

# i = 0
# while i != 3:
#      i = random.randint(1,6)
#      print(i)

# list = [11,22,33,44,55,66,77]
# print(random.choice(list))

# for lotto in range(6):
#     i = random.randint(1,45)
#     print(i,end=' ')

#break, continue

# x = 0
# while True:
#     print(x)
#     x += 1
#     if x == 10:
#         break
# for i in range(10000) :
#     print(i)
#     if i == 100:
#         break

# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(i)

# i = 0
# while i > 10:
#     if i % 2 == 0:
#         continue
#      print(i)

# for i in range(100000):
#     pass
#
# print(10)

# for i in 값1:    5
#     for i in 값2:   3
#         실행문


# for i in range(5):
#     for j in (5):
#         print('*',end='')
#         print()

# *
# **
# ***
# ****
# *****

# for i in range(1,6):
#      for j in range(i):
#          print('*',end='')
#      print()

# *****
# ****
# ***
# **
# *
# for i in range(5,0,-1):
#     for j in range(i):
#         print('*',end='')
#     print()

# for i in range(5):
#     for j in range(5):
#         if i <= j:
#            print('*',end='')
#         else:
#            print(' ',end='')
#     print()
#리스트와 튜플에 활용 append: 요소 하나를 추가
# append: 요소 하나를 추가
# extend: 리스트를 연결하여 확장
# insert: 특정 인덱스에 요소 추가

# a = [10,20,30]
# print(a)
# a.append(500)
# print(a)
# a.extend([600,700])
# print(a)
# a.append([800,900])
# print(a)
# a.insert(2,1000)
# print(a)
# a.insert(len(a),[800,1000])
# print(a)
# a[1:1] = [200,300]
# print(a)

# 리스트 요소 삭제
# pop: 마지막 요소 또는 특정 인덱스의 요소를 삭제
# remove: 특정 값을 찾아서 삭제
# a = [10,20,30]
# a.pop()
# print(a)
# a = [10,20,30]
# del  a[1]
# print(a)
# a = [10,20,30]
# a.remove(20)
# print(a)

# a = [10,20,30,15,20,40]
# print(a.index(20))
# print(a.count(20))
# a.reverse()
# print(a)
# index(값)은 리스트에서 특정 값의 인덱스를 구합니다
# count(값)은 리스트에서 특정 값의 개수를 구합니다
# reverse()는 리스트에서 요소의 순서를 반대로 뒤집습니다
# sort() 또는 sort(reverse=False): 리스트의 값을 작은 순서대로 정렬(오름차순)
# sort(reverse=True): 리스트의 값을 큰 순서대로 정렬(내림차순)
# clear()는 리스트의 모든 요소를 삭제합니다
# a.sort()
# print(a)
# a.sort(reverse=True)
# print(a)
# a.clear()
# print(a)

# a = [10, 20, 30]
# a[len(a):] = [500]
# print(a)

# a = [10,20,30,40,50]
# b = a
# b[2] = 99
# print(a)
# print(b)

# b = a.copy()
# b[2] = 99
# print(a)
# print(b)

# for i in [23,45,67,87,53]:
#     print(i,end=" ")

# a = [23,45,67,87,53]
# for i in range(len(a)):
#     print(a[i],end=' ')


# a = [23,45,67,87,53]
# for index,value in enumerate(a,start=1):
#     print(index,value)

# a = [23,45,67,87,53]
# i = 0
# while i < len(a):
#     print(a[i])
#     i += 1

# a = [23,45,67,87,53]
# a.sort()
# print(a)
# print('최소값',a[0])
# a.sort(reverse=True)
# print(a)
# print('최대값',a[0])
#
# print(max(a))
# print(min(a))

# a = [ 1,2,3,4,5,6,7,8,9,10]
# sum = 0
# for i in a:
#     sum += i
# print(sum)

#리스트 표현식
# for i in range(10):
#     print(i)

# a = [i for i in range(10)]
# print(a)
# #range
# a = [i * 2 for i in range(10)]
# print(a)
# a = [i for i in range(10) if i % 2 == 0]
# print(a)

#map
#list(map())
#tuple(map())
# a = list(map(str,range(10)))
# print(a)

# 2차원 리스트
# from pprint import pprint
# a = [[10, 20],
#      [30, 40],
#      [50, 60]]
# pprint(a,indent = 4,width = 20)
# print(a)
# print(a[0][0])
# print(a)[1][1]
# a[2][1] =100
# print(a)

# a = [[10, 20],
#      [30, 40],
#      [50, 60]]

# for x,y in a:
#     print(x,y)
#
# for i in a:
#     for j in i:
#         print(j,end=" ")
#     print()

# for i in range(len(a)):
#     for j in range(len(a[i])):
#         print(a[i][j],end=' ')
#     print()
#while 반복문 한번 사용
# i = 0
# while i < len(a):
#     x, y = a[i]
#     print(x,y)
#     i += 1
# while 반복문을 두 번 사용
# a = [[10, 20], [30, 40], [50, 60]]
#
# i = 0
# while i < len(a):
#     j = 0
#     while j < len(a[i]):
#         print(a[i][j], end=' ')
#         j += 1
#     print()
#     i+=1

# a = [10,20]
# x = a[0]
# y = a[1]
# x,y = a
# print(x,y)

# a = [[10, 20],
#      [30, 40],
#      [50, 60]]

# i = 0
# while i < len(a):
#     x,y = a[i]
#     print(x,y,end=' ')
#     i += 1
#     print()

# i = 0
# while i < len(a):
#     j = 0
#     while j < len(a[i]):
#         print(a[i][j], end= ' ')
#         j += 1
#     i += 1
#     print()

# a = []
# for i in range(10):
#     a.append(i)
#
# print(a)


#a = [[0,0],[0,0],[0,0]]
# a = []
# for i in range(3):
#     line = []
#     for j in range(2):
#         line.append(0)
#     a.append(line)
#
# print(a)

# a = [1,2,3]
# b = [4,5,6]
# print(a+b)
# print(a*b)

# a = [[0 for j in range(2)] for i in range(3)]
# print(a)
# a = [[0] * 2 for i in range(3)]
# print(a)

# a = [[10, 20],
#      [30, 40],
#      [50, 60]]
#
# b = a   #얕은복사
# import copy
# b = a.copy() #얕은복사
# b = copy.deepcopy(a)# 깊은 복사

#문자열 응용
# s = 'Hello world'
# s = s.replace('world','python')
# # s = 'Hello world'.replace('world','python')
# print(s)
# s = 'app bpp cpp'.split(',')
# print(s)
#
# s = ' '.join(['app','bpp','cpp'])
# print(s)
# print('python'.upper())
# print('PYTHON'.lower())
# s = '  PYTHON    '.lstrip()
# print(s)
# s = ' PYTHON '.rstrip()
# print(s)
# s = ' PYTHON '.strip()
# print(s)
# s = ',PYTHON. '.strip(',.')
# print(s)
#
# s = 'PYTHON'.ljust(10)
# print(s)
# s = 'PYTHON'.rjust(10)
# print(s)
# s = 'PYTHON'.center(10)
# print(s)
# s = 'PYTHON'.rjust(10).upper()
# print(s)
# s = 'apple pineapple'
# print(s.find('pl'))
# print(s.rfind('pl'))
# print(s.find('xy'))
# print(s.index('pl'))
# # print(s.index('xy'))
# print(s.count('pl'))
#
# print('I am %s' % 'james')
# print('I am %10s' % 'james')
# print('I am %-10s' % 'james')
# print('I am %d year old' % 20)
# print('I am %f weight' % 62.3)
# print('I am %.2f weight' % 62.3)
# print("Today is %d %s" %(3,'April'))

# print("Hello {0}".format('world'))
# print("Hello {0}".format(100))
# print("Hello {0} {1} {2}".format('world','script',3.8))
# print("Hello {0} {0} {1} {1}".format('world','script',3.8))
# print("Hello {} {} {}".format('world','script',3.8))
# print("Hello {len} {ver}".format(len='python',ver=3.8))
#
# len = 'python'
# ver = 3.9
# print(f'Hello {len}{ver}')

# print('{0:<10}'.format('python'))
# print('{0:>10}'.format('python'))
# print('{0:@<10}'.format('python'))
# print('{0:@>10}'.format('python'))

# print(format(123456,","))
# print('{0:,}'.format(123456))
# x = {'a':16,'b':20, 'c':30 ,'d':40}
# print(x)
# x.update(a = 90)
# print(x)
# x.update(a = 900, f=60)
# print(x)
#
# y = {1:'ome',2:'two'}
# y.update([[2,'two'],[4,'FOUR']])
# print(y)
# y.update(zip([1,2],['one','two']))
# print(y)
# y[5] = 'Five'
# print(y)

# x = {'a':16,'b':20, 'c':30 ,'d':40}
# # x.pop('a')
# # del  x['b']
# x.popitem()
# x.clear()
# print(x)
#
# x = {'a':10,'b':20, 'c':30 ,'d':40}
# print(x.get('a'))
#
# #items,keys,values
# print(x.items())
# print(x.keys())
# print(x.values())
#
# #리스트와튜플믈 딕셔너리로 변경
# keys=['a','b','c','d']
# x = dict.fromkeys(keys)
# print(x)

# x = {'a':10,'b':20, 'c':30 ,'d':40}
#
# for i in x:
#     print(i, end=" ")
#
# for key velue in x.items():
#     print(key, value)
#
# for key in x.key():
#     print(key)
#
# for value in x.values()
#     print(value)

# keys=['a','b','c','d']
# x = {key:value for key , value in dict.fromkeys(keys).items()}
# print(x)

# x = {'a':10,'b':20, 'c':30 ,'d':40}

# for key,value in x.items():
#     if value == 20:
#         del x [key]

# print(x)

# x = {'a':10,'b':20, 'c':30 ,'d':40}
# x = {key:value for key,value in x.items() if value != 20}
# print(x)

# x = {'a':{'python:''2.7'},'b':{'python':'3.6'}}
# print(x['a'])
# x['b']['python'] = '3.9'
# print(x)

# dict_list = []
# while True:
#     sel = int(input('1번은 딕셔너리 생성 2번은 종료'))
#     if sel == 1:
#         print("요소추가")
#         my_dict={}
#         while True:
#             key = int(input('key입력:'))
#             val = input('value입력:')
#             my_dict[key] = val
#             con = int(input('1번은 딕셔너리 생성 2번은 종료'))
#             if con == 2:
#                 print('입력종료')
#                 break
#         dict_list.append(my_dict)
#     elif sel == 2:
#         print('입력종료')
#         break
#     else:
#         print('잘못입력하셨습니다')
#         break
# print("결과 :",dict_list)

#set
#중복을 허용하지 않는다
#시퀸스 객체가 아니다.
#집합연산
# x={1,2,3,4,5}
# print(x)
#
# x = set(range(5))
# print(x)

# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}

#합집합
# print(set.union(a, b))
# print(a|b)
# #차집합
# print(a-b)
# #교집합
# print(a&b)
# #대칭차집합
# print(a^b)


# a = {1, 2, 3, 4}
# a |= {5}
# print(a)
# a -= {3}
# print(a)

# a = {1,2,3,4}
# a.add(5)
# print(a)
# a.remove(4)
# print(a)
# a.pop()
# a.clear()
# print(a)

# a = {1,2,3,4,5}
# for i in a:
#     print(i)
#
# a = {i for i in "apple"}
# print(a)

#파일 사용하기
#open()
#write()/read()
#clsoe()

# file = open('hello.txt','w')
# file.write('hello world')
# file.close()

# file = open('hello.txt','r')
# s = file.read()
# print(s)
# file.close()

# with open('hello.txt','r') as file:
#     s = file.read()
#     print(s)

# with open('hello.txt','w') as file:
#     for i in range(3):
#         file.write('hello world {0}'.format(i))
#
# lines = ['안녕하세요\n','파이썬\n','코딩도장 입니다\n']
# with open('hello.txt','w') as file:
#     file.writelines(lines)
#
# with open('hello.txt','r') as file:
#     lines = file.readlines()
#     print(lines)

# with open('hello.txt','r') as file:
#     lines = None
#     while lines != '':
#         lines = file.readline()
#         print(lines.strip('\n'))

# with open('hello.txt','r') as file:
#     for line in file:
#         print(line.strip('\n'))

#함수사용하기
#def 함수명():
#         실행문

#함수의 정의
# def hello():
#     print('hello world') #pass

#함수의 호출
# hello()


# def add(a,b):
#     print(a + b)
#
#
# a,b = map(int,input().split())
# add(a,b)

# def add(a,b):
    # sum = a + b
    # return sum
# add(10,20)
# sum = add(10,20)
# print(sum)
# print(add(10,20))

# print(sum([1,2,3,4,5]))
# print(max([1,2,3,4,5]))

# def ten(a):
#     if a == 10:
#         return
#     print(a)
# ten(10)
# def add_sub(a,b):
#     return a+b , a-b

# x,y= add_sub(20,30)
# print('합:',x)
# print('차',y)

# def number(a,b,c):
#     print(a)
#     print(b)
#     print(c)

# number(1,2,3)

# x =[1,2,3]
# number(*x)

# x =[1,2,3]
# a,b,c = x
# print(a,b,c)

#가변인수
# print(1,2,3,4,5,6,7,8,9)
# def number2(*args):
#     for i in args:
#         print(i)

#number2(1,2,3,4,5,6,6,7)
# x = [10,20,30,40,50]
# number2(*x)

# def per(name,age,address):
#     print('이름',name)
#     print('나이',age)
#     print('주소',address)
#
# per('홍길동',30,'서울시 용산구 이촌동')
# p = {'name':'홍길동','age':30,'address':'용산'}
# per(**p)

# def per2(**kwargs):
#     for kw, arg in kwargs.items():
#         print(kw, ': ', arg, sep='')
# per2(name='홍길동')
# p = {'name':'홍길동','age':30,'address':'용산'}
# per2(**p)

# def per3(name,age,addr='비공개'):
#     print('이름',name)
#     print('나이',age)
#     print('주소',addr)
#
# per3('홍길동',20)

#람다 표현식
# def plus(x):
#     return x + 10
# plus(10)

# plus = lambda x: x + 10 #익명함수
# print(plus(50))
#
# list = list(map(plus,[1,2,3]))
# print(list)
#
# list = list(map(lambda x: x + 10, [1, 2, 3]))
# print(list)

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list = list(map(lambda x: str(x) if x % 3 == 0 else x,a))
# print(list)

# a = [1,2,3,4,5]
# b = [2,3,4,5,6]
#
# list = list(map(lambda x,y: x+y,a,b))
# print(list)

# a = [1,2,5,6,8,3,4,7]
# list = list(filter(lambda x: x> 5 and x < 10,a))
# print(list)

# a = [1,2,3,4,5,6,7,8,9,10]
# from functools import reduce
# print(reduce(lambda x,y: x + y, a))

#클래스(객체를 표현하는 형식)
#속성(변수),기능(함수)
# class 클래스명:
#       속성(변수)
#       기능(함수)

#클래스의 정의
# class person:
#     def greeting(self): #self 필수.
#         print('안녕하세요')

#클래스의 생성(메모리 활당)
# james = person()
#클래의 맴버의 참조
# james.greeting()

# class Hello:
#     pass

# class person:
#     def __init__(self):
#         self.name = '홍길동'
#         self.hello ='안녕하세요'
#
#     def greeting(self):
#         print(self.hello,self.name)

# james = person()
# james.greeting()

# class person:
#     def __init__(self,name,age,addr):
#         self.name = name
#         self.age = age
#         self.addr = addr
#     def greeting(self):
#         print('{0} 저는 {1} 입니다'.format(self.name,self.age,self.addr))
# james = person('제임스',100,'인천')
# james.greeting()
# print(james.name)
# print(james.age)
# print(james.addr)

# class person:
#     bag = [] #클래스의 변수
#     def put_bag(self,stuff):
#         self.bag.append(stuff)
#
# james = person()
# james.put_bag('열쇠')
#
# maria = person()
# maria.put_bag('책')
#
# print(james.bag)
# print(maria.bag)

# class person:
#     def __init__(self):
#         self.bag = []
#
#     def put_bag(self,stuff):
#         self.bag.append(stuff)
#
# james = person()
# james.put_bag('gun')
#
# maria = person()
# maria.put_bag('bullet')
#
# print(james.bag)
# print(maria.bag)

#정적 메소드/클래스메소드
#정적 메소드는 self빼고 쓴다
# class calc:
#     @staticmethod
#     def add(a,b):
#         print(a+b)
#     @staticmethod
#     def mul(a,b):
#         print(a*b)
#
# calc.add(1,3)
# calc.mul(3,5)

# class person:
#     count = 0
#     def __init__(self):
#         person.count += 1
#
#     @classmethod
#     def print_count(cls):
#         print('{0}'.format(cls.count))
#
#     @classmethod
#     def create(cls):
#         p = cls()    # cls()로 인스턴스 생성
#         return p
#
# james = person()
# maria = person()
# park = person.create()
#
# person.print_count()

#예외처리

# def div(x):
#     return 10 / x
# print(div(2))
# print(div(0))


# try:
#     x = int(input('숫자 입력:'))
#     y = 10 / x
#     print(y)
# except:
#     print('0으로 정수를 나누지 마세요')

# y = [10,20,30]

# try:
#     index,x = map(int,input('인덱스와 나눌 숫자를 입력하세요:').split())
#     print(y[index] / x)
# except ZeroDivisionError as e:         # 숫자를 0으로 나눠서 에러가 발생했을 때 실행됨
#         print('숫자를 0으러 나누지 마세요',e)
# except IndexError as e:
#         print('잘못된 인덱스 번호입니다',e)
# else:                                  # try의 코드에서 예외가 발생하지 않았을 때 실행됨
#     print("예외가 발생 하지 않음")
# finally:                               # 예외 발생 여부와 상관없이 항상 실행됨
#     print('예외 발생 유무와 상관없이 실행')

# try:
#     x = int(input('3의 배수를 입력하세요'))
#     if x % 3 != 0:
#         raise  Exception('3의 배수가 아닙니다.')
#     print(x)
# except Exception as e:
#     print('예외 발생 처리',e)

#예외 만들기

# class NotreeMulerror(Exception):
#     def __init__(self):
#         super().__init__('3의 배수가 아닙니다')
#
# def mul():
#     try:
#         x = int(input('3의 배수를 입력하세요'))
#         if x % 3 != 0:
#             raise NotreeMulerror()
#         print(x)
#     except NotreeMulerror as e:
#         print('예외 발생',e)
#
# mul()

#정규식표현
import re
# print(re.match('hello','hello world')) // 시작하는
# print(re.match('world','hello world')) 글자 찾음
# print(re.search('hello','hello world')) //위치 상관없이 일치하는
# print(re.search('world','hello world')) 글자 찾음

# print(re.match('hello|world','hello'))
# print(re.match('[0-9]*','1234'))
# print(re.match('[0-9]+','1234'))
# print(re.match('[0-9]+','abcd'))

# print(re.search('hello', 'hello world'))
# print(re.match('hello','hello world'))
# print(re.search('^hello', 'hello world'))
# print(re.search('world$','hello world'))

# print(re.match('h?','h'))
# print(re.match('h?','hi'))
# print(re.match('h.','h'))
# print(re.match('h.','hi'))

# print(re.match('[0-9]{3}','hello'))
# print(re.match('[0-9]{2,3}','hello'))
# print(re.match('(hello){3}','hellohellohello'))

# print(re.match('[0-9]{3}-[0-9]{3,4}-[0-9]{4}','010-419-3429'))
# print(re.match('[a-zA-Z0-9]*','hello1234'))
# print(re.match('[a-zA-Z0-9]*','hello1234'))
# print(re.match('[a-zA-Z0-9]+','hello'))
# print(re.match('[a-zA-Z0-9]+','@'))
# print(re.match('[^A-Z]+','hello'))
# print(re.match('^[A-Z]+','Hello'))
# print(re.match('[0-9]+$','hello1234'))
# print(re.search('[0-9]+$','hello1234'))
# print((re.search('\*+','1**2')))
#
# #특수문자 $, ( , )
# print(re.match('[$()a-zA-Z0-9]','$(document)'))
# #공백문자
# print(re.match('[a-zA-Z0-9\s]+','hello world123'))
#그룹화 하기
# m = re.match('([0-9]+) ([0-9]+)','10 259')
# print(m.group(1))
# print(m.group(2))
# print(m.group())
# m = re.match('(?P<func>[a-zA-z_][a-zA-Z0-9_]+)\((?P<arg>\w+)\)','print(1234)') // ?P <이름>
# print(m.group('func'))                                                         // 그룹화 이름만들기
# print(m.group('arg'))
# [a-z]

# re.sub('apple|orange','fruit','apple box orange tree') #sub패턴', '바꿀문자열', '문자열', 바꿀횟수
# re.sub('[0-9]+','n','1 2 Fizz 4 Buzz Fizz 7 8')

#모튤과 패키지

# import math
# print(math.pi)
# print(math.sqrt(4))

# import math as m
# print(m.pi)
#
# from  math import  pi,sqrt
# print(pi)
# print(sqrt(4))
#
# from math import pi as p,sqrt as s
# print(s(4))
# print(p)


# import urllib.request      #import 폴더명, 폴더명.~~~.파일명
# rep = urllib.request.urlopen('http://www.google.com')
# print(rep.status)

# from  urllib.request import Request, urlopen
# req = Request('http://www.google.co.kr')
# response = urlopen(rep)
# response.status

# import requests
# r = requests.get('http://www.google.com')
# print(r.status_code)
#시험 연습
# a = "a:b:c:d"
# b = a.replace(":","#")
# print(b)
a = [1,3,5,4,2]
a.sort()  # sort를 사용하여 리스트 값들을 먼저 정렬한 후 reverse함수를 사용하여 순서를 뒤집는다
a.reverse()
print(a)