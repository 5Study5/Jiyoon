def solution(n, lost, reserve):
    
    # 반복 전에 lost, reserve 둘 다 포함된 학생 처리
    common = set(lost) & set(reserve)

    lost = list(set(lost) - common)
    reserve = list(set(reserve) - common)

    # 정렬
    lost.sort()
    reserve.sort()
    
    answer = n - len(lost)
    
    for i in range(len(lost)):
        if(lost[i]-1 in reserve):
            answer += 1
            reserve.remove(lost[i]-1)
        elif(lost[i]+1 in reserve):
            answer += 1
            reserve.remove(lost[i]+1)
    
    return answer