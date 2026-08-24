# 통과
def solution(citations):

# h개 이상 논문이 h번 이상 인용
# H-Index 는 h의 최댓값

    n = len(citations)   # 논문 개수     
    
    for h in range(n, -1, -1):  # <---- 가능한 최대의 값인 n부터 시작
        
        # h번 이상 인용된 논문 개수
        num_or_over_h = 0    
        for i in range(n):
            if ( citations[i]>= h ):
                num_or_over_h += 1
        
        if(num_or_over_h >= h): # h번 이상 인용된 논문이 h편 이상
            return h



# 실패했던 풀이
def solution(citations):

# 발표한 논문 개수: n = len(citations)
# h개 이상 논문이 h번 이상 인용 + 나머지 논문(n-h-a개)이 h번 이하 인용
# H-Index 는 h의 최댓값

    n = len(citations)   # 논문 개수     
    h_max = 0
    
    for h in range(n+1):  # <----- range (n) 하면 n 미포함! h = n 인 경우 고려 못 함!!!
        
        # h번 이상 인용된 논문 개수
        num_or_over_h = 0    
        for i in range(n):
            if ( citations[i]>= h ):
                num_or_over_h += 1
        
        if(num_or_over_h >= h): # h번 이상 인용된 논문이 h편 이상
            h_max = h
            
    
    return h_max