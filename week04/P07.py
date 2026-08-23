def solution(board, h, w):
    
    n = len(board)
    count = 0            # 같은 색으로 색칠된 칸의 개수
    
    dh = [0,1,-1,0]
    dw = [1,0,0,-1]
    
    for i in range(4):
        h_check = h + dh[i]
        w_check = w + dw[i]
        if( 0 <= h_check and h_check < n ) and ( 0 <= w_check and w_check < n ):
            if(board[h][w]==board[h_check][w_check]):
                count += 1        
    
    return count