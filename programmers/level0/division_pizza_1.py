import math

def solution(n):
    if n <= 7:
        return 1
    
    else:
        # math.ceil(수) 는 올림값이 리턴된다.
        return math.ceil(n/7)