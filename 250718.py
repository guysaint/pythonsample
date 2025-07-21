from typing import List
import collections
import heapq
# nums = [1,3,-1,-3,5,3,6,7]
# k = 3

# def maxSlidingWindow(nums: List[int], k: int):
#     if not nums:
#         return nums
#     
#     r = []
#     for i in range(len(nums) -k + 1):
#         r.append(max(nums[i:i + k]))
#         
#     return r

# def maxSlidingWindow(nums: List[int], k: int):
#     results = []
#     window = collections.deque()
#     current_max = float('-inf')
#     for i, v in enumerate(nums):
#         window.append(v)
#         if i < k - 1:
#             continue
#         
#     # 새로 추가된 값이 기존 최댓값보다 큰 경우 교체
#         if current_max == float('-inf'):
#             current_max = max(window)
#         elif v > current_max:
#             current_max = v
#             
#         results.append(current_max)
#         
#         #최댓값이 윈도우에서 빠지면 초기화
#         if current_max == window.popleft():
#             current_max = float('-inf')
#     return results
# print(maxSlidingWindow(nums, k))
      

#
# S = "AD0BEC0DEBANC"
# T = "ABC"

# def minWindow(s: str, t: str):
#     def contains(s_substr_lst: List, t_lst: List):
#         for t_elem in t_lst:
#             if t_elem in s_substr_lst:
#                 s_substr_lst.remove(t_elem)
#             else:
#                 return False
#         return True
#     
#     if not s or not t:
#         return ''
#     
#     window_size = len(t)
#     
#     for size in range(window_size, len(s) +1):
#         for left in range(len(s) - size +1):
#             s_substr = s[left:left + size]
#             if contains(list(s_substr), list(t)):
#                 return s_substr
#     return ''


# 
# def minWindow(s: str, t: str):
#     need = collections.Counter(t)
#     missing = len(t)
#     left = start = end = 0
#     
#     #오른쪽 포인터 이동
#     for right, char in enumerate(s, 1):
#         missing -= need[char] > 0
#         need[char] -= 1
#         
#         #필요 문자가 0이면 왼쪽 포인터 이동 판단
#         if missing ==0:
#             while left < right and need[s[left]] < 0:
#                 need[s[left]] += 1
#                 left += 1
#                 
#             if not end or right - left <= end - start:
#                 start, end = left, right
#                 need[s[left]] += 1
#                 missing += 1
#                 left += 1
#     return s[start:end]                
# 
# print(minWindow(S,T))

# s = "AAABBC"
# k = 2
# 
# def characterReplacement(s: str, k: int):
#     left = right = 0
#     counts = collections.Counter()
#     for right in range(1, len(s) + 1):
#         counts[s[right - 1]] += 1
#         
#         #가장 흔하게 등장하는 문자 탐색
#         max_char_n = counts.most_common(1)[0][1]
#         
#         #k 초과시 왼쪽 포인터 이동
#         if right - left - max_char_n > k:
#             counts[s[left]] -= 1
#             left += 1
#     return right - left
# 
# print(characterReplacement(s,k))


#주식을 사고팔기 가장 좋은 시점
# a = [7,1,5,3,6,4]
# def maxProfit(prices: List[int]):
#     result = 0
#     
#     for i in range(len(prices) - 1):
#         if prices[i + 1] > prices[i]:
#             result += prices[i + 1] - prices[i]
#     return result
#         
# print(maxProfit(a))

#키에 따른 대기열 재구성
height = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
def reconstructQueue(people: List[List[int]]):
    heap = []
    
    for person in people:
        heapq.heappush(heap, (-person[0], person[1]))
        
    result = []
        
    while heap:
        person = heapq.heappop(heap)
        result.insert(person[1], [-person[0], person[1]])
    return result
print(reconstructQueue(height))