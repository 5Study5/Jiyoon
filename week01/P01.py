def solution(array, commands):
    answer = []
    
    cnt = len(commands)
    
    for index in range(cnt):
        
        i,j,k = commands[index]
        sliced_array = array[i - 1:j]
        sliced_array.sort()
        
        num = sliced_array[k-1]
        answer.append(num)
    
    return answer