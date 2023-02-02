'''
연결 리스트를 뒤집어라.
input:
    head = [1,2,3,4,5]
    head = [1,2]
    head = []
output:
    [5,4,3,2,1]
    [2,1]
    []
'''

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        첫 번째 풀이. 재귀
        다음 노드 next와 현재 노드 node를 파라미터로 지정한 함수를 계속해서 재귀 호출
        node.next에는 이전 prev리스트를 계속 연결해주면서 node가 None이 될 때까지 재귀 호출
        백트래킹되면서 연결 리스트가 거꾸로 연결됨.
        맨 처음 리턴된 prev는 뒤집힌 연결 리스트의 첫 번째 노드가 됨.
        '''
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev
            
            next, node.next = node.next, prev
            
            return reverse(next, node)
        
        return reverse(head)
        
        '''
        두 번째 풀이. 반복문
        위와 비슷한 풀이. node가 None이 될 때 prev는 뒤집힌 연결 리스트의 첫 번째 노드가 됨.
        반복이 재귀에 비해 70% 수준의 메모리를 차지해 공간 복잡도는 좀 더 낮은 편.
        '''
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev