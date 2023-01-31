'''
정렬되어 있는 두 연결 리스트를 합쳐라
input 예:
    1 -> 2 -> 4, 1 -> 3 -> 4
output 예:
    1 -> 1 -> 2 -> 3 -> 4 -> 4
'''
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        첫번째 풀이. 재귀
        '''
        if (not list1) or (list2 and list1.val > list2.val):
            '''
            list1이 없거나,
            list1.val과 list2.val의 값을 비교 후 list1.val의 값이 더 크면서 list2가 존재하면
            더 작은 값을 왼쪽으로
            '''
            list1, list2 = list2, list1
        
        if list1:
            list1.next = self.mergeTwoLists(list1.next, list2)
        
        return list1