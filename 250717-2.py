#가장 큰 수 만드는 게임
import random
import time

tries = 3 #3번의 기회
time_limit = 15 # 시간 제한 15초

length = random.randint(2,8) # 2~8개까지 랜덤으로 숫자 생성
a = [str(random.randint(0,99)) for _ in range(length)] # 0~99까지 생성된 숫자를 문자열 리스트로 만듦
original = a[:]
print("랜덤 생성된 리스트: ", original)
print("가장 큰 수를 만드세요.\n")

# 생성된 리스트를 비교하여 가장 큰 수를 만듦
for i in range(len(a)): 
    for j in range(len(a) - i - 1):
        if a[j] + a[j + 1] < a[j + 1] + a[j]:
            # 자리 바꾸기
            a[j], a[j + 1] = a[j + 1], a[j]

result = ''.join(a)   #변수에 정답을 저장해놓음

while tries > 0: # 오답 3번까지 기회를 줌
    start_time = time.time() #입력 시간 시작
    ans = str(input("정답: "))
    
    cntdown = time.time() - start_time
    
    if cntdown > time_limit:
        #print(f"시간 초과!!(cntdown:.2f}초) 기회를 잃었습니다.\n")
        print(f"⏰ 시간 초과!({cntdown:.2f}초) 기회를 잃었습니다.\n")
        tries -= 1
        continue
    if ans == result:
        print(f"정답입니다! {cntdown:.2f}초 만에 맞추셨어요!")
        break
    else:
        tries -= 1
        if tries > 0:
            print(f"틀렸어요. 다시 시도하세요. 남은기회: {tries}번, ({cntdown:.2f}초 소요)\n")
            
if tries == 0:
    print(f"모든 기회 소진! 정답은 {result}였습니다.")      


'''
from functools import cmp_to_key

# 비교 함수 정의: x + y 와 y + x를 비교해서 큰 쪽이 앞에 오게
def compare(x, y):
    if x + y > y + x:
        return -1  # x가 앞에 와야 함
    elif x + y < y + x:
        return 1   # y가 앞에 와야 함
    else:
        return 0   # 같음

# 입력 받기
a = list(map(str, input("숫자들을 쉼표로 구분해 입력하세요: ").split(",")))

# 정렬 (비교함수를 이용해 정렬)
a.sort(key=cmp_to_key(compare))

# 모두 0으로 이루어진 경우 예외 처리
if a[0] == '0':
    print("가장 큰 수: 0")
else:
    print("가장 큰 수:", ''.join(a))
'''

