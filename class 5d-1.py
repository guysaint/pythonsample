'''
selected = None
while selected not in ['가위', '바위', '보']:
    selected = input("가위, 바위, 보 중 하나를 선택하세요: ")
print(f"당신이 선택한 것은 {selected}입니다.")
'''
'''
st = 'programming'
for ch in st:
    if ch in ['a', 'e', 'i', 'o', 'u']:
        continue
    print(ch, end=' ')
print()
print('The end')
'''
'''
def print_star(n):
    for i in range(n):
        return = none
        for j in range(n):
            print("*", end=' ')
        print("*************************")

print_star(4)
'''
'''
def print_sub(a,b):
    m = a - b
    print(a,"과", b,"의 차는", m, "입니다.")

print_sub(10, 20)
'''
'''
def multiples(n,m):
    tup = ()
    for i in range(1, m+1):
        tup += (i*n,)
    return tup
r1, r2, r3, r4 = multiples(3,4)
print(r1, r2, r3, r4)
r1, r2, r3, r4, r5 = multiples(2,5)
print(r1, r2, r3, r4, r5)
'''

def print_sum():
    a = 100
    b = 200
    result = a + b
    print('print_sum() 내부:', a, '과', b, '의 합은', result, '입니다.')

a = 10
b = 20
print_sum()
result = a + b
print('print_sum() 외부:', a, '과', b, '의 합은', result, '입니다.')
