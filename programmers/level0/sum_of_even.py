def solution(n):
    if n == 0:
        return 0
    
    sum_a = 0
    
    for i in range(2, n+1, 2):
        sum_a += i
    
    return sum_a