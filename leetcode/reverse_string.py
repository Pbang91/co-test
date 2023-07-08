'''
문자열을 뒤집는 함수를 작성하라. 입력값은 문자 배열이며, 리턴없이 리스트 내부를 직접 조작하라.
input:
    ["h", "e", "l", "l", "o"]
output:
    ["o", "l", "l", "e", "h"]

input:
    ["H", "a", "n", "n", "a", "h"]

output:
    ["h", "a", "n", "n", "a", "H"]
'''

from typing import List

def reverse_string_list1(str_list: List[str]) -> None:
    '''
    첫번째 풀이
    '''
    str_list.reverse()
    print(str_list)

def reverse_string_list2(str_list: List[str]) -> None:
    '''
    두번째 풀이
    '''
    left_index, right_index = 0, len(str_list) - 1

    while left_index < right_index:
        str_list[left_index], str_list[right_index] = str_list[right_index], str_list[left_index]

        left_index += 1
        right_index -= 1

    print(str_list)


str_list1 = ["h", "e", "l", "l", "o"]
str_list2 = ["H", "a", "n", "n", "a", "h"]
str_list3 = ["h", "e", "l", "l", "o"]
str_list4 = ["H", "a", "n", "n", "a", "h"]

reverse_string_list1(str_list1)
reverse_string_list1(str_list2)
reverse_string_list2(str_list3)
reverse_string_list2(str_list4)