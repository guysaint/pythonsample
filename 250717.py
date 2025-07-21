# def Bubblesort(A):
#     for i in range(1, len(A)):
#         for j in range(0, len(A) - 1):
#             if A[j] > A[j + 1]:
#                 A[j], A[j + 1] = A[j + 1], A[j]
#     return A                
# a = [1,4,2,5,7,3]                
# print(Bubblesort(a))

#두 정렬 리스트 병합
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2

    def sortList(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head

        # 러너 기법
        half, slow, fast = None, head, head
        while fast and fast.next:
            half, slow, fast = slow, slow.next, fast.next.next
        half.next = None

        l1 = self.sortList(head)
        l2 = self.sortList(slow)
        return self.mergeTwoLists(l1, l2)

# 숫자 입력
nums = list(map(int, input("숫자를 쉼표로 구분해 입력하세요: ").split(",")))

# 숫자 리스트를 연결 리스트로 변환
def build_linked_list(nums):
    if not nums:
        return None
    head = ListNode(nums[0])
    current = head
    for n in nums[1:]:
        current.next = ListNode(n)
        current = current.next
    return head

# 연결 리스트 출력
def print_linked_list(head):
    while head:
        print(head.val, end=" -> " if head.next else "\n")
        head = head.next

# 실행
head = build_linked_list(nums)
solution = Solution()
sorted_head = solution.sortList(head)

print("정렬된 결과:")
print_linked_list(sorted_head)
