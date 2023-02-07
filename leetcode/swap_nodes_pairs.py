'''
연결 리스트를 입력받아 페어단위로 스왑하라
input:
    1 -> 2 -> 3 -> 4
output:
    2 -> 1 -> 4 -> 3
'''
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        첫 번째 풀이. 값만 스왑
        '''
        cur = head

        while cur and cur.next:
            # 여기서 값만 교환
            cur.val, cur.next.val = cur.next.val, cur.val

            cur = cur.next.next
        
        return head
        '''
        두 번재 풀이. 반복 구조
        '''
        root = perv = ListNode(None)

        prev.next = head

        while head and head.next:
            # b가 a(head)를 가리키도록 할당
            b = head.next
            head.next = b.next
            b.next = head
            # prev가 b를 가리키도록 할당
            prev.next = b
            # 다음번 비교를 위해 이동
            head = head.next
            prev = prev.next.next
        
        return root.next
        '''
        세 번째 풀이. 재귀
        '''
        if head and head.next:
            p = head.next
            # 스왑된 값을 리턴받아서
            head.next = self.swapPairs(p.next)
            p.next = head

            return p
        
        return head