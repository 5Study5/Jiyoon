def solution(schedules, timelogs, startday):
    answer = 0
    
    
    # 출근 +10분
    # 토, 일 X
    # h*100 + m
    
    n = len(schedules)   # 직원 수
    
    hope = []
    for i in range(n):
        k = int(schedules[i])
        hope.append((k//100)*60 + k%100)  # 분으로 변환


    # 직원 한 명씩 검사
    for i in range(n):
        success = True

        d = startday - 1
        # startday 1 2 3 4 5 6 7 
        #          월화수목 금 토 일
        # d : 0 ~ 6 -> 월 ~ 일 

        for j in range(7):
            if (d != 5) and (d != 6): # 토, 일 제외

                t = int(timelogs[i][j])
                real_t = (t//100)*60 + t%100
                if(real_t > (hope[i]+10)):
                    success = False     # 10분 초과 시, 탈락
                    break
                
            d = (d+1)%7
            
        if success:
            answer += 1
    
    return answer