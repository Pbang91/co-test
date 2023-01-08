'''
덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.
input 예:
    nums = [2, 7, 11, 15], target = 9
output 예:
    [0, 1]

nums[0] + nums[1] = 2 + 7 = 9
'''
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        첫번재 풀이. 브루트포스
        '''
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        '''
        두번째 풀이. 해쉬 테이블 형식
        '''
        nums_map = {}

        for i, v in enumerate(nums):
            find_value = target - v
            
            if find_value in nums_map:
                return [nums_map[find_value], i]

            nums_map[v] = i

test_case = Solution()
case_result1 = test_case.twoSum([2,7,11,15], 9)
case_result2 = test_case.twoSum([3,2,4], 6)
case_result3 = test_case.twoSum([3,3], 6)
case_result4 = test_case.twoSum([-3,4,3,90], 0)

print(case_result1, case_result2, case_result3, case_result4, sep="\n")