def solution(n, w, num):
    cnt = 0
    
    # n : 전체 상자 수
    # w : 한 층의 상자 수
    # num : 찾으려는 상자 번호
    
    boxes = [[0]*w for _ in range(n//w+1)]
    
    # 숫자 채우기
    k=1
    for row in range(n//w +1): # index 0부터 시작
            for col in range(w): # 0 ~ w-1
                if(k > n):
                    break
                else:
                    if(row%2==0):
                        boxes[row][col] = k
                        k += 1
                    else:
                        boxes[row][w-col-1] = k 
                        k += 1
                
    # print(boxes)
    
    # num의 위치 찾기
    f = num // w     # num의 층수
    if (num % w == 0):
        f -= 1
    
    num_i = boxes[f].index(num)
    
    # 상자 개수 count
    for i in range(f,n//w+1):
        if boxes[i][num_i] != 0:
            cnt += 1
    
    return cnt