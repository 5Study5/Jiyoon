def solution(n):
    answer = []
    
    n_str = str(n)
    num = len(n_str)
    
    for i in range(num):
        m = n%10
        answer.append(m)
        n = n//10
        
    
    return answer