'''
#1부터 n까지 연속한 정수의 곱을 구하는 알고리즘
def factorial(n):
    fac = 1
    for i in range(1,n+1):
        fac = fac * i
    return fac


    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

    
n = int(input("숫자를 입력하세요: "))   
print(f"{n}의 팩토리얼은 {factorial(n)}입니다.")
'''
'''
# 1부터 n까지의 합 구하기를 재귀 호출로
def total(n):
    if n <=0:
        return 0
    else:
        return n + total(n-1)
    
n = int(input("숫자를 입력하세요: "))
print(f"1부터 {n}까지의 합은 {total(n)}입니다.")
'''

'''
# 숫자 n개 중에서 최댓값 찾기를 재귀 호출로

def abs_max(n,m):
    for i in range(1, len(n)):
        if n[i] <= 0:
            return n
        else:
            max = n > abs_max(n-1)
            return max

n = list(map(int, input("숫자를 입력하세요").split(",")))
print("두 수 중 큰 수는", abs_max(n), "입니다.")
'''
'''
# 4와 6의 최대 공약수를 찾는
def max_divisor(a,b):
    if a>b:
        for i in range(2,a):
            res = a % i
            res2 = b % i
            if res == 0 & res2 ==0:
                max = i
                return max
            
    else:
        for i in range(2,b):
            res = a % i
            res2 = b % i
            if res == 0 & res2 ==0:
                max = i
                return max
            
           
    
a, b = map(int, input("숫자 두개를 입력하세요: ").split(","))
print("최대 공약수는", max_divisor(a,b),"입니다.")
'''
'''
def gcd(a,b):
    i = min(a,b)
    while True:
        if a % i == 0 & b % i == 0:
            return i
        i = i - 1
    
a, b = map(int, input("숫자 두개를 입력하세요: ").split(","))
print("최대 공약수는", gcd(a,b),"입니다.")
'''
'''
def gcd(a,b):
    if b ==0: #종료조건
        return a
    return gcd(b, a % b) #좀 더 작은 값으로 자기 자신을 호출

a, b = map(int, input("숫자 두개를 입력하세요: ").split(","))
print("최대 공약수는", gcd(a,b),"입니다.")
'''
'''
import turtle as t
def spiral(sp_len):
    if sp_len <= 5:
        return
    t.forward(sp_len)
    t.right(90)
    spiral(sp_len -5)
    t.speed(0)
    spiral(200)
    t.hideturtle()
    t.done()
'''
'''
#하노이탑 옮기기
cnt = 0
def hanoi(n, from_pos, to_pos, aux_pos):

    if n ==1:
        global cnt
        cnt += 1
        print(from_pos, "->", to_pos,": ",cnt)
        return
    hanoi(n -1, from_pos,aux_pos, to_pos)
    
    cnt += 1
    print(from_pos, "->", to_pos,": ",cnt)
    hanoi(n - 1, aux_pos, to_pos, from_pos)
print("n = 1")
hanoi(1,1,3,2)
print("n=2")
hanoi(2,1,3,2)
print("n=3")
hanoi(3,1,3,2)
print("n=8")
hanoi(8,1,3,2)
'''

def search_list(a,x):
    n = len(a)
    for i in range(0,n):
        if x == a[i]:
            return i
    return -1

v = [17, 92, 18, 33, 58, 7 ,33, 42]
print(search_list(v, 18))
print(search_list(v, 33))
print(search_list(v, 900))