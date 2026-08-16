def solution(brown, yellow):

    # W >= H
    
    # brown + yellow = 전체 격자 개수 = 전체 크기 = W * H
    # brown = W * 2 + (H-2) * 2 = 2*(W+H-2)
    
    total = brown + yellow
    for i in range(2, total):
        if ( total%i == 0):  # i는 total의 약수이면서,
            j = total/i
            if (brown == 2*(i+j-2)):  # 등식 만족
                return [max(i,j), min(i,j)]