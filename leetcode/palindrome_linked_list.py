'''
연결 리스트가 팰린드롬 구조인지 판별하라
input 예:
    1 -> 2
output 예:
    false

input 예:
    1 -> 2 -> 2 -> 1
output 예:
    true
'''
from typing import Optional

import collections
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        '''
        첫번째 풀이. 단순 리스트 풀이
        '''
        q = []

        if not head:
            return True

        node = head

        while node is not None:
            q.append(node.val)
            node = node.next
        
        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False
        
        return True
        '''
        두번째 풀이. Deque 풀이. 기본 로직은 리스트와 같지만 앞 뒤 추출이 O(1)이 걸리니 더 나은 풀이.
        '''
        q = collections.deque()

        if not head:
            return True
        
        node = head

        while node is not None:
            q.append(node.val)
            node = node.next
        
        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False
        
        return True

test_case = Solution()

linked_list1 = ListNode(val=1)
linked_list2 = ListNode(val=2)

linked_list1.next = linked_list2

linked_list3 = ListNode(val=1)
linked_list4 = ListNode(val=2)
linked_list5 = ListNode(val=2)
linked_list6 = ListNode(val=1)

linked_list3.next = linked_list4
linked_list4.next = linked_list5
linked_list5.next = linked_list6

case_result1 = test_case.isPalindrome(linked_list1)
case_result2 = test_case.isPalindrome(linked_list2)

print(case_result1, case_result2, sep='\n')