from typing import List
import bisect


# def search(self, nums: List[int], target: int) -> int:
#     def binary_search(left, right):
#         if left <= right:
#             mid = (left + right) //2
#             
#             if nums[dim] < target:
#                 return binary_search(mid + 1, right)
#             elif nums[mid] > target:
#                 return binary_seartch(left, mid - 1)
#             else:
#                 return mid
#     return binary_search(0, len(nums) -1)
# 
# def search(self, nums: List[int], target: int) -> int:
#     left, right = 0, len(nums) -1
#     while left <= right:
#         mid = (left + right) //2
#         
#         if nums[mid] < target:
#             left = mid + 1
#         elif nums[mid] > target:
#             right = mid - 1
#         else:
#             return mid
#     return -1
# 
# def search(nums: List[int], target: int) -> int:
#     index = bisect.bisect_left(nums, target)
#     
#     if index < len(nums) and nums[index] == target:
#         return index
#     else:
#         return -1
#     
# num = sorted([3,1,4,2])
# print(search(num, 1))


# 2d 행렬 검색을 이용한 보물 찾기 게임
# 매번 랜덤하게 생성되는 보물의 위치를 좌표값으로 찾는 게임

import random

def generate_sorted_matrix(n, min_val=1, max_val=100):
    flat = list(range(1, n*n+1))
    matrix = [flat[i * n:(i + 1) * n] for i in range(n)]
    return matrix

def print_board(n, board):
    print("\n ", "  ".join([f"{i:2}" for i in range(n)]))
    for i, row in enumerate(board):
        print(f"{i:2}", "   ".join(row))
    print()

n = 5
matrix = generate_sorted_matrix(n)
treasure_row = random.randint(0, n - 1)
treasure_col = random.randint(0, n - 1)
treasure = matrix[treasure_row][treasure_col]

# 시각적 보드: 숨김 상태
board = [["." for _ in range(n)] for _ in range(n)]

print("🏝️ 보물 찾기 게임 시작!")
print(f"{n}x{n} 격자에 보물이 숨겨져 있습니다.")
print("숫자는 정렬되어 있으며 좌표를 추리하며 보물을 찾으세요!")
print("시도한 칸은 X / 정답은 O 로 표시됩니다.\n")

MAX_ATTEMPTS = 7
attempts = 0

while attempts < MAX_ATTEMPTS:
    print_board(n, board)

    try:
        user_input = input(f"🔍 시도 {attempts + 1}/{MAX_ATTEMPTS} - 좌표 입력 (row,col): ")
        row, col = map(int, user_input.strip().split(","))
        if not (0 <= row < n and 0 <= col < n):
            print("⚠️ 범위를 벗어났습니다. 0부터", n - 1, "까지 입력하세요.\n")
            continue

        guess = matrix[row][col]
        attempts += 1

        if guess == treasure:
            board[row][col] = "O"
            print_board(n, board)
            print(f"🎉 정답입니다! 보물은 ({row},{col})에 숨겨져 있었습니다.")
            break
        elif guess < treasure:
            board[row][col] = "X"
            print(f"📈 {guess}는 보물보다 작습니다.\n")
        else:
            board[row][col] = "X"
            print(f"📉 {guess}는 보물보다 큽니다.\n")

    except ValueError:
        print("⚠️ 입력 형식이 잘못되었습니다. 예: 2,3\n")

if attempts == MAX_ATTEMPTS and guess != treasure:
    board[treasure_row][treasure_col] = "O"
    print_board(n, board)
    print(f"💀 실패! 정답은 ({treasure_row},{treasure_col}) → {treasure}였습니다.")
