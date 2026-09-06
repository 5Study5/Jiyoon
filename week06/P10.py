def solution(elements):
    sums = set()
    
    # 수열의 최대 길이는 len(elements)
    # 합 저장하는 set 만들고, set 길이 반환.
    n = len(elements)  # 수열의 원소 개수
    
    for k in range(n):  # 수열의 첫번째 요소의 인덱스 k
        p = 0
        for i in range(n): # 수열의 길이 = i+1
            index = (k+i)%n
            p += elements[index]
            sums.add(p)
    
    return len(sums)


# timeout 시간초과 풀이
# def solution(elements):
#     sums = set()
    
#     # 수열의 최대 길이는 len(elements)
#     # 합 저장하는 set 만들고, set 길이 반환.
#     n = len(elements)  # 수열의 원소 개수
    
#     for i in range(1, n+1): # 수열의 길이
        
#         for k in range(n):  # 수열의 첫 요소 elements[k] 지정
#             p = 0
#             for j in range(i): # 수열의 길이만큼 반복
#                 index = (k+j)%n
#                 p += elements[index]
#             sums.add(p)
    
#     return len(sums)