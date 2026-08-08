def solution(park, routes):
    answer = []
    
    row = 0
    col = 0
    H = len(park)
    W = len(park[0])
    
    for i in range(len(park)):
        if 'S' in park[i]:
            row = i
            col = park[i].find('S')
        
    
    for i in range(len(routes)):

        op = routes[i][0]
        n = int(routes[i][2])
        
        row_t = row
        col_t = col
        
        possible = True
        
        for j in range(n):
            
            if(op =='E'):
                col_t += 1
            elif (op =='W'):
                col_t -= 1
            elif (op =='S'):
                row_t += 1
            elif (op =='N'):
                row_t -= 1

            if (row_t<0 or col_t<0 or row_t>H-1 or col_t>W-1):
                possible = False
                break

            if (park[row_t][col_t]=='X'):
                possible = False
                break
        
        if possible:
            row = row_t
            col = col_t
        
    answer = [row, col]
    
    return answer