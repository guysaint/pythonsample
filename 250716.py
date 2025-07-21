'''
# 정렬 알고리즘
def find_ins_idx(r,v):
    for i in range(0, len(r)):
        if v < r[i]:
            return i
    return len(r)

def ins_sort(a):
    result =[]
    while a:
        value = a.pop(0)
        ins_idx = find_ins_idx(result, value)
        result.insert(ins_idx, value)
    return result
d = [2,4,5,1,3]
print(ins_sort(d))

'''

'''
def BubbleSort(ary):
    n = len(ary)
    for end in range(n-1,0,-1):
                    for cur in range(0, end):
                        if(ary[cur] > ary[cur+1]):
                            ary[cur], ary[cur+1] = ary[cur+1], ary[cur]
    return ary

dataAry = [188, 162, 168, 120, 50, 150, 177, 105]
print('정렬 전 -->', dataAry)
dataAry = BubbleSort(dataAry)
print('정렬 후 -->',dataAry)
'''
'''
def merge_sort(a):
    n = len(a)
    if n <= 1:
        return a
    mid = n //2
    g1 = merge_sort(a[:mid])
    g2 = merge_sort(a[mid:])

    result = []
    while g1 and g2:
        if g1[0] < g2[0]:
            result.append(g1.pop(0))
        else:
            result.append(g2.pop(0))

    while g1:
        result.append(g1.pop(0))
    while g2:
        result.append(g2.pop(0))
    return result

d= [6,8,3,19, 10,1,2,4,7,5]
print(merge_sort(d))
'''

#거품 정렬

def bubble_sort(a):
    n = len(a)
    while True:
        changed = False

        for i in range(0, n - 1):
            if a[i] > a[i + 1]:
                print(a)
                a[i], a[i + 1] = a[i + 1], a[i]
                changed = True

        if changed == False:
            return
d=[2,4,5,1,3]
bubble_sort(d)
print(d)