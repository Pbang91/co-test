'''
역순으로 저장된 연결 리스트의 숫자를 더하라.
input:
    (2 -> 4 -> 3) + (5 -> 6 -> 4)
output:
    7 -> 0 -> 8

342 + 465 = 807
'''
from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    '''
    첫 번째 풀이. 문자열 변환
    '''
    def revers_list(self, head : ListNode) -> ListNode:
            node, prev = head, None

            while node:
                next, node.next = node.next, prev

                prev, node = node, next

            return prev
        
    def to_list(self, node : ListNode) -> List:
        convert_list : List = []

        while node:
            convert_list.append(node.val)
            node = node.next

        return convert_list
    
    def to_reversed_linked_list(self, result : str) -> ListNode:
        prev : ListNode = None

        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node
        
        return node

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = self.to_list(self.revers_list(l1))
        b = self.to_list(self.revers_list(l2))

        result_str = int(''.join(str(e) for e in a)) + int(''.join(str(e) for e in b))
        # result_str = int(''.join(map(str, a))) + int(''.join(map(str, b)))

        return self.to_reversed_linked_list(str(result_str))
        '''
        두 번째 풀이. 전가산기 구현
        '''
        root = head = ListNode(0)

        carry = 0

        while l1 or l2 or carry:
            total_sum = 0

            if l1:
                total_sum += l1.val
                l1 = l1.next
            
            if l2:
                total_sum += l2.val
                l2 = l2.next

            carry, val = divmode(total_sum + carry, 10)
            head.next = ListNode(val)
            head = head.next

        return root.next