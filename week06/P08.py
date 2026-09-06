def solution(arr):
    answer = []
    
    answer.append(arr[0])  # index 0은 그냥 추가
    
    for i in range(1, len(arr)): # 1 ~ len(arr)-1
        if arr[i] != arr[i-1]:
            answer.append(arr[i])
        else: continue
    
    return answer


# a[-1:]   # 마지막 요소 반환 (리스트 형식)
# a[-1]    # 마지막 요소 반환 (값 형식)

# if arr[i] != answer[-1]:
# 이렇게 바꿔도 됨