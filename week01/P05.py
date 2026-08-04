def solution(n):
    answer = ''
    
    A = '수박'
    
    p = n//2
    q = n % 2
    
    if(n%2==0):
        str = "수박" * p
    else:
        str = "수박" * p
        str += '수'
    
    answer = str
    
    return answer