'''
높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 계산하라.
input 예:
    [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
output 예:
    6
'''
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        첫번째 풀이. 투 포인트 이동
        '''
        if not height:
            return 0
        
        left, right, volume = 0, len(height) - 1, 0
        left_max, right_max = height[left], height[right] #각 포인터에서 가장 긴 벽을 정해준다.
        
        while left < right:
            # 현재 가장 긴 벽과 이동된 포인터의 값 중에서 큰 값을 결정해주고
            left_max, right_max = max(left_max, height[left]), max(right_max, height[right])
            # 왼쪽과 오른쪽에서 가장 긴 벽을 비교해서 왼쪽이 작거나 같으면
            # 현재 물에다 가장 긴 벽과 현재 포인터의 값을 뺀 양을 더해주자
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            # 그게 아니면 오른쪽에서 위와 같은 로직을 진행해주자
            else:
                volume += right_max - height[right]
                right -= 1
            
        return volume
        '''
        두번째 풀이. 스택(학습 더 필요)
        '''
        if not height:
            return 0
        
        stack, volume = [], 0

        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
            
                top = stack.pop()
            
                if not len(stack):
                    break
            
                distance = i - stack[-1] - 1
                
                waters = min(height[i], height[stack[-1]]) - height[top]
                
                volume += distance * waters
            
            stack.append(i)
        
        return volume

test_case = Solution()
case_result1 = test_case.trap([0,1,0,2,1,0,1,3,2,1,2,1])
case_result2 = test_case.trap([4,2,0,3,2,5])

print(case_result1, case_result2, sep="\n")