def solution(answers):
    answer = []
    
    n_1, n_2, n_3 = 0, 0, 0   # 각 각 맞춘 문제 수
    arr_2 = [2,1,2,3,2,4,2,5]
    arr_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i in range(len(answers)):
        
        X= answers[i]
        
        # 1번
        if ( X == i%5 +1 ):
            n_1 += 1
        
        # 2번
        j = i%8
        if (X == arr_2[j]):
            n_2 += 1
        
        # 3번
        k = i%10
        if (X == arr_3[k]):
            n_3 += 1
    
    n = [n_1, n_2, n_3]
    
    for i in range(3):
        if(max(n) == n[i]):
            answer.append(i+1)
    
    return answer