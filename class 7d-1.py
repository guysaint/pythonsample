'''
days_list = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
days_set = set(days_list)
print(days_set)
fruits_tuple = ('apple', 'orange', 'watermelon') #튜플
fruits_set = set(fruits_tuple) #튜플로부터 집합 만들기
print(fruits_set)

h_str = 'hello' # 문자열
h_set = set(h_str)  # 문자열로부터 집합 만들기
print(h_set) # 집합은 문자 'l'의 중복을 허용하지 않음
'''
'''
def product_set(set1, set2):
    res = set()
    for i in set1:
        for j in set2:
            res = res | {(i, j)} # 이중 for 루프를 이용한 곱집합
    return res

A = {1, 3}
B = {2, 4}
AxB = product_set(A, B)
print('A =', A)
'''
'''
import datetime
print(datetime.datetime.now())
today = datetime.date.today()
print(today)
print(dir(datetime))
'''
'''
import datetime as dt
start_time = dt.datetime.now()
start_time.replace(month = 12, day =25)
print(dt.datetime(2024,12,25,7,1,25,880317))
'''
'''
from datetime import datetime
start_time = datetime.now()
start_time.replace(month = 12, day = 25)
print(datetime(2024, 12, 25, 7, 1, 25, 880317))
'''
'''
import datetime as dt
today = dt.date.today()
print(f'오늘은 {today.year}년 {today.month}월 {today.day}일입니다.')

xMas = dt.datetime(2026, 12, 25)
gap = xMas - dt.datetime.now()

print(f'크리스마스까지 {gap.days}일 {gap.seconds // 3600}시간 남았습니다.')
'''
'''
import time
print("바로 출력되는 구문.")
time.sleep(4.5)
print("4.5초 후에 출력되는 구문.")
'''
'''
import time
start_time = time.time()
print(234+5+2134+53451435+4+12456+1234+1234+1234+124124214+1256777878)
end_time = time.time()
gap = end_time - start_time
print('1에서 10까지의 합을 구하고 출력하는 시간:{:7.4f}초'.format(gap))
'''
'''
import random as rd
L= [rd.randrange(0,101,5), rd.randrange(0,101,5), rd.randrange(0,101,5)]
print(L)
print(rd.randrange(0,101,5))
'''
'''
def pseudo_rand(x):
    a = 1103515245
    b = 12345
    m = 2** 31
    new_x = (a* x + b) % m
    return new_x

seed = 100
x = pseudo_rand(seed)
print(x)
x = pseudo_rand(x)
print(x)
'''
'''
import random as rd
lotto_list = list(range(1, 46))
rd.shuffle(lotto_list) 
lotto_list = lotto_list[:6]
lotto_list.sort()
print('이번 주의 추천 로또 번호:', lotto_list)

'''
'''
import sys
print(sys.prefix)
print(sys.version)
print(sys.copyright)
'''
'''
import turtle
turtle.setup(width = 400, height = 400)
t = turtle.Turtle()
t.shape('turtle')
t.speed(5)
for i in range(3):
    t.forward(100)
    t.left(120)
    
turtle.done()
'''

'''
import turtle
turtle.setup(width = 400, height = 400)
t = turtle.Turtle()
t.speed(100)
n = 100
length = 5
for i in range(n):
    t.left(360/n)
    t.forward(length)

turtle.done()
'''
'''
import turtle
t = turtle.Turtle()
t.circle(100)
turtle.done()
'''
'''
import turtle
t=turtle.Turtle()

for i in range(1,11):
    t.setheading(90)
    t.circle(10*i)
    t.setheading(270)
#for i in range(1, 11):
    t.circle(10*i)
turtle.done()
'''
'''
import turtle
t = turtle.Turtle()
corlor = ['red', 'green', 'blue', 'orange']
turtle.bgcolor('black')
t.speed(50)

for i in range(200):
    t.pencolor(corlor[i % 4])
    t.forward(i)
    t.left(93)

turtle.done()
'''
'''
import turtle
import random as rd

t = turtle.Turtle()
t.shape('circle')
d = 300
for i in range(40):
    x = rd.randint(-d, d)
    y = rd.randint(-d, d)
    t.goto(x, y)

turtle.done()
'''
'''

from tkinter import *

window = Tk()
window.geometry("400x200")
label = Label(window, text = '헬로 파이썬')
label.pack()

window.mainloop()
'''
'''
from tkinter import *
window = Tk()
input_entry = Entry(window, width=50)
input_entry.pack()

button = Button(window, text='처리')
button.pack()
label = Label(window, text=' ')
label.pack()

window.mainloop()
'''

from tkinter import *

window = Tk()
window.title("계산기")
window.geometry("300x200")

Label(window, text = '숫자 1').grid(column = 0, row = 0)
Label(window, text = '숫자 2').grid(column = 0, row = 1)
res_label = Label(window, text = "결과")
res_label.grid(column = 0, row = 2)

num1 = Entry(window, width = 10)
num2 = Entry(window, width = 10)
num1.grid(column = 1, row = 0)
num2.grid(column = 1, row = 1)

def add():
    answer = float(num1.get()) + float(num2.get())
    res_text = f'결과 = {answer}'
    res_label.configure(text = res_text)

def subtract():
    answer = float(num1.get()) - float(num2.get())
    res_text = f'결과 = {answer}'
    res_label.configure(text = res_text)

def multiplication():
    answer = float(num1.get()) * float(num2.get())
    res_text = f'결과 = {answer}'
    res_label.configure(text = res_text)

def division():
    answer = float(num1.get()) / float(num2.get())
    res_text = f'결과 = {answer}'
    res_label.configure(text = res_text)

btn_plus = Button(window, text = '+', command = add)
btn_minus = Button(window, text = '-', command = subtract)
btn_multi = Button(window, text = '*', command = multiplication)
btn_div = Button(window, text = '/', command = division)

btn_plus.grid(column = 2, row = 1)
btn_minus.grid(column = 3, row = 1)
btn_multi.grid(column = 4, row = 1)
btn_div.grid(column = 5, row = 1)

window.mainloop()
