def solution(d, budget):
    answer = 0
    
    # 모두 더한 값에서 가장 큰 것부터 제외시킴 (정렬)
    
    n = len(d)    # 전체 부서 개수로 초기화
    
    total = sum(d)
   # total = 0 
   # for i in range(n):
   #     total += d[i]
    
    rep = n

    # 최댓값 꺼내기
    # copy = d.copy()
    # for i in range(rep):
    #     if (total > budget):
    #         total -=  max(copy)  # -> O(n)
    #         n -= 1
    #         copy.remove(max(copy))
    #     else:
    #         break
            
    # 혹은 정렬 후 꺼내기
    copy = d.copy()
    copy.sort(reverse = True)
    for i in range(rep):
        if (total > budget):
            total -= copy[i]  # -> O(1)
            n -= 1
        else:
            break
    
    return n