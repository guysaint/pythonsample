'''
def print_star(n=1):
    for i in range(n):
        print("**************************")
print_star()
'''
'''
def div(a, b = 2):
    return a / b

print('div(4) =', div(4))
print('div(6, 3) =', div(6, 3))
'''
'''
def get_root(a, b, c):
    r1 = (-b +(b ** 2 -4 * a * c) **0.5) / (2 * a)
    r2 = (-b -(b ** 2 -4 * a * c) **0.5) / (2 * a)
    return r1, r2

#result1, result2 = get_root(1, 2, -8)
#result1, result2 = get_root(a = 1, c = -8, b = 2))
print('해는', result1, '또는', result2)

'''
'''
def func(shape, width=1, height=1, radius=1):
    if shape ==0:
        return width * height
    if shape ==1:
        return 3.14 * radius ** 2

print('rect area = ', func(0, width = 10, height = 2))
print('circle area =', func(1, radius=5))
'''
'''
def greet(*names):
    for name in names:
        print('안녕하세요', name, '씨')
        print('인자의 개수:', len(names))
greet('홍길동', '양만춘', '이순신')
greet('Jmaes', 'Thomas')
'''
'''
def sum_nums(*numbers):
    result = 0
    for n in numbers:
        result += n
    return result
print(sum_nums(10, 20, 30))
print(sum_nums(10, 20, 30, 40, 50))
'''
'''
def sum_sums(*numbers):
    avg = 0
    sum = 0
    count = 0

    for n in numbers:
        count = count + 1
        sum = sum + n
    avg = sum / count

    print(count, '개의 인자', numbers)
    print('합계:', sum,',평균:',avg)

sum_sums(10, 20, 30)
sum_sums(10, 20, 30, 40, 50)
'''
'''
def factorial(n):
    if n <= 1 :
        return 1
    else:
        return n * factorial(n-1)
n = 5
print('{}! = {}'.format(n, factorial(n)))
'''
'''
name = 'YoungCoder'
string = f'congo, {name}'
print(string)
'''
'''
for i in range(2, 15, 2):
    print('{0:3d} {1:4d} {2:5d}'.format(i, i*i, i*i*i))
'''
'''
print('{0:10.3f}'.format(3.1415926))
print('{0:10.4f}'.format(3.1415926))
print('{:,}'.format(1234567890))
'''
'''
a_str = 'Hello Python!'
print(id(a_str)
'''
'''
a_list = ['a', 'b', 'c', 'd', 'e']
print(a_list.append('f'))
print(a_list)
print(10 in a_list)
'''

'''
n_list = [11,22,33,44,55]
if (55 in n_list):
    n_list.remove(55)
if 88 in n_list:
    n_list.remove(88)
print(n_list)
'''
'''
print_list = [2,3,5,7]
print_list.append(11)
print(print_list)
print_list.remove(3)
print(print_list)
'''
'''
nations = ['Korea', 'China', 'Russia', 'Malaysia']
if 'Nepal' not in nations:
    nations.append('Nepal')
    print(nations)
if 'Japan' not in nations:
    print('Japan은 국가 목록에 없습니다.')

if 'Russia' in nations:
    print('Russia는 국가 목록에 있습니다.')
    '''
'''
list1 = [10,20,30,40,50]
i = 0
for n in list1:
    list1[i] = n * 10
    i = i + 1

print(list1)
'''

list1 = [10,20,30,40,50,60,70,80]
print(list1[0:9])
print(list1[:])
print(list1[:5])
print(list1[1:-2])
print(list1[::-1])

print(list1)

