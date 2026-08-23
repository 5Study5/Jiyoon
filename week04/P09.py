def solution(k, score):
    answer = []
    
    # HOF = score[:k].sort(reverse=True)
    n = len(score)
    
    for i in range(min(n,k)): # k > n 인 경우도 고려해야 함...;
        arr = score[:i+1]    # i '+1' : '<' 이므로  
        answer.append(min(arr))
        print(min(arr))
    
    for i in range(k, n):
        # arr = score[:i+1].sort(reverse=True) # sort()는 None 반환!
        arr = sorted( score[:i+1], reverse = True)
        answer.append(arr[k-1])
        print(arr[k-1])
        
    return answer