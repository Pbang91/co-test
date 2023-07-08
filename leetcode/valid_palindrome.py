'''
주어진 문열이 팰린드롬인지 확인하라. 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.
input 예:
    "A man, a plan, a canal: Panama"

output 예:
    true

input 예:
    "race a car"

output 예:
    false
'''
import collections
import re
from typing import Deque, List


def is_palindrome1(text: str) -> str:
    '''
    첫번째 풀이
    '''
    format_text = re.sub(r"[^a-zA-Z0-9]", "", text).lower()
    
    count = len(format_text)
    first_index = 0
    last_index = len(format_text) - 1
    
    while count != 0:
        start_text = format_text[first_index]
        end_text = format_text[last_index]

        if start_text != end_text:
            return "false"
            
        count -= 1
        first_index += 1
        last_index -= 1
    
    return "true"

def is_palindrome2(text: str) -> str:
    text_arr: List[str] = []

    for char in text:
        if char.isalnum():
            text_arr.append(char.lower())
    
    while len(text_arr) > 1:
        if text_arr.pop(0) != text_arr.pop():
            return "false"
    
    return "true"

def is_palindrome3(text: str) -> str:
    text_queue: Deque = collections.deque()

    for char in text:
        if char.isalnum():
            text_queue.append(char.lower())
    
    while len(text_queue) > 1:
        if text_queue.popleft() != text_queue.pop():
            return "fasle"
    
    return "true"

def is_palindrome4(text: str) -> str:
    new_text = text.lower()

    format_text = re.sub(r"[^a-zA-Z0-9]", "", new_text)

    if format_text == format_text[::-1]:
        return "true"
    
    return "false"

text_1 = "A man, a plan, a canal: Panama"
text_2 = "race a car"

result1 = is_palindrome1(text_1)
result2 = is_palindrome1(text_2)
result3 = is_palindrome2(text_1)
result4 = is_palindrome2(text_2)
result5 = is_palindrome2(text_1)
result6 = is_palindrome2(text_2)
result7 = is_palindrome2(text_1)
result8 = is_palindrome2(text_2)

print(result1, result2, result3, result4, result5, result6, result7, result8, sep="\n")