'''
try:
    a, b = input('두 수를 입력하시오: ').split()
    result = int(a) / int(b)
    print('{}/{} = {}'.format(a, b, result))
except:
    print('수가 정확한지 확인하세요.')
    '''
'''
try:
    b = 2/0
    a = 1 + 'hundred'
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except TypeError:
    print('자료형이 맞지 않습니다.')
'''
'''
try:
    a, b = input('두 수를 입력하시오: ').split()
    result = int(a) / int(b)
    
except ZeroDivisionError:
    print('오류 : 0으로 나눔을 시도했습니다.')
except ValueError:
    print('오류: 입력 값이 정수나 실수가 아닙니다.')
except:
    print('오류: 10 2와 같이 두 정수를 입력하세요')
else:
    print('{}/{} = {}'.format(a, b, result))

'''
'''
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print('0으로 나누는 오류 발생')
    else:
        print('결과 :', result)
    finally:
        print('수행 완료')

print('divide(100, 2) 함수호출 :')
divide(100, 2)
print('divide(100, 0) 함수호출 :')
divide(100, 0)
 '''
'''
f = open(r'c:\pythonsample\test.txt', 'r')
s = f.read()
print(s)
f.close()
'''
'''
f = open(r'c:\pythonsample\test.txt', 'r')
s = f.readline()
print(s, end = '')
s = f.readline()
print(s, end = '')
f.close()
'''
'''
f = open(r'c:\pythonsample\test.txt', 'a+')
f.write('This will be appended.\n')
f.write('This too.\n')
f.close()
'''
'''
f = open(r'c:\pythonsample\test.txt', 'r', encoding = 'UTF8')
s = f.read()
print(s, end = '')
'''
'''

class PersonalInfo:

#Class attribute
    nationality = 'Korean'

#Initalize, Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #Instance method
    def getPersonalInfo(self):
        print('Name:', self.name)
        print('Age:', self.age)

    #Instance method
    def ageGroup(self):
        if self.age < 30:
            return 'under 30'
        else:
            return 'over 30'
    
#create an instance object
personal_choi = PersonalInfo('CK Choi', 25)
personal_choi.getPersonalInfo()
print('Age Group:', personal_choi.ageGroup())
print('Nationality:', personal_choi.nationality)
'''
'''
class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return f'Cat(name={self.name}, color = {self.color})'
        
    def meow(self):
        print(f'내 이름은 {self.name}, 색깔은 {self.color}','야옹 야옹~~~')

nabi = Cat('나비', '검은색')
nero = Cat('네로', '흰색')
mimi = Cat('미미', '갈색')
nabi.meow()
nero.meow()
mimi.meow()
nabi = Cat('나비', 3)
print(nabi)
nabi.color = -5
print(nabi)
'''

'''
class Cat:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __str__(self):
        return f'Cat(name = {self.__name}, age = {self.__age})'
    
    def set_age(self, age):
        if age > 0:
            self.__age = age

    def get_age(self):
        return self.__age
nabi = Cat('나비', 3)
print(nabi)
nabi.set_age(4)
nabi.set_age(-5)
print(nabi)
'''
'''
class A:
    PI = 3.14

class B(A):
    pass

a = A()
b = B()
print('a.PI =', a.PI)
print('b.PI =', b.PI)
'''

'''
class Person:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name
    

class Manager(Person):
    def __init__(self, name, position):
        Person.__init__(self, name)
        self.position = position
    
    def info(self):
        return f'관리직 :{self.get_name()}, 직책: {self.position}'

class Employee(Person):
    def __init__(self, name, salary=100):
        Person.__init__(self, name)
        self.salary = salary
    def get_salary(self):
        return f'종업원 : {self.get_name()}, 급여 : {self.salary}'


cto = Manager('박동민', '최고기술책임자(CTO)')
worker1 = Employee('박동윤', 320)
worker2 = Employee('홍승주', 250)

print(cto.info())
print(worker1.get_salary())
print(worker2.get_salary())
'''
'''
class Person:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name
    

class Manager(Person):
    def __init__(self, name, position):
        super().__init__(name)          #super()는 부모클래스의 메서드를 호출, super() = person 이고 인자가 (self, name)에서 (name)만 사용
        self.position = position
    
    def info(self):
        return f'관리직 :{self.get_name()}, 직책: {self.position}'

class Employee(Person):
    def __init__(self, name, salary=100):
        super().__init__(name)
        self.salary = salary
    def get_salary(self):
        return f'종업원 : {self.get_name()}, 급여 : {self.salary}'


cto = Manager('박동민', '최고기술책임자(CTO)')
worker1 = Employee('박동윤', 320)
worker2 = Employee('홍승주', 250)

print(cto.info())
print(worker1.get_salary())
print(worker2.get_salary())        
'''
'''
def adult_func(n):
    if n >= 19:
        return True
    else:
        return False
    
ages = [15, 20, 25, 30, 18, 54]
print('성년 리스트 :')
for a in filter(adult_func, ages):
    print(a, end=' ')
'''
'''
ages = [15, 20, 25, 30, 18, 54]

print('성년 리스트')
for a in filter(lambda x: x >= 19,ages):
    print(a, end=' ')
    '''

def square(x):
    return x ** 2

a = [1,2,3,4,5,6,7]
square_a = list(map(square, a))
print(square_a)