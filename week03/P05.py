def solution(sizes):
    
    max_ = 0
    min_ = 0
    
    for i in range(len(sizes)):
        i_max = max(sizes[i][0], sizes[i][1])
        i_min = min(sizes[i][0], sizes[i][1])
        
        max_ = max(i_max, max_)
        min_ = max(i_min, min_)
        
    return max_*min_