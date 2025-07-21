
import math
'''
def abs_sign(a):
    if a >=0:
        return a
    else:
        return -a
t = int(input("Enter a number: "))

def abs_square(a):
    b = a*a
    return math.sqrt(b) # 제곱근

print(abs_sign(t))
print()
print(abs_square(t))
'''
'''
total = 0
def abs_plus(a):
    for i in range(1, a+1):
        
        global total
        total = total + i
    return total
    
n = int(input("Enter a number: "))
print(abs_plus(n))
'''

'''
print("1부터 n까지 정수의 합을 구하시오")
n = int(input("n: "))

sum = 0
i = 1

while i <=n:
sum += i
i += 1

print("1부터", n, "까지의 정수의 합은", sum, "입니다.")
'''
'''
def abs_squareplus(n):
    sum = n*(n+1) * (2*n+1) // 6

    return sum

n = int(input("Enter a number: "))
print("1부터", n, "까지의 정수의 제곱의 합은", abs_squareplus(n), "입니다.")
'''
'''
def abs_max(a, b):
    if a > b:
        return a
    else:
        return b

a,b = map(int, input("숫자를 입력하세요").split) 
print("두 수 중 큰 수는", abs_max(a, b), "입니다.")
'''

'''
def abs_max2(a):
    max_value = a[0]
    for i in range(1, len(a)):
        if a[i] > max_value:
            max_value = a[i]
           
    return max_value
'''
'''
def find_max_idx(a):
    max_idx = 0
    for i in range(1, len(a)):
        if a[i] > a[max_idx]:
            max_idx = i
    max_idx += 1        
    return max_idx

aa = list(map(int, input("숫자를 입력하세요").split(",")))
print("입력한 숫자 중 가장 큰 수는", find_max_idx(aa),"번째 숫자입니다.")
'''
'''
def abs_min(a):
    min_value = a[0]
    for i in range(1, len(a)):
        if a[i] < min_value:
            min_value = a[i]
        
    return min_value

aa = list(map(int, input("숫자를 입력하세요").split(",")))
print("입력한 숫자 중 가장 작은 수는", abs_min(aa),"입니다.")
'''
s = set()

def match_name(a):
    for i in range(1, len(a)):
        for j in range(i):
          
            if a[i] == a[j]:
                print("중복된 이름은", a[i],"입니다.")
                s.add(a[i])
    
    return s


n = list(map(str, input("이름을 입력하세요: ").split(",")))
print("입력한 이름 중 중복된 이름은", match_name(n), "입니다.")
print(s)