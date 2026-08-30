from collections import Counter

def solution(k, tangerine):
    answer = 0
    
    # collections.Counter(arr)를 사용하면 각 원소의 개수를 딕셔너리로 반환
    count = Counter(tangerine)
    
    # 빈도수가 높은 순서대로 상위 n개의 원소를 (원소, 개수) 형태의 튜플 리스트로 반환
    # 숫자를 넣지 않으면 전체 원소 정렬하여 반환
    for size, num in count.most_common():
        k -= num
        answer += 1

        if k <= 0:
            break
    
    return answer