def solution(numbers):
    answer = 0
    
    # split 에 숫자 하나씩 저장
    split=[]
    for n in numbers:
        split.append(int(n))
    
    # 만들어진 숫자들 저장
    nums = set()
    
    # 숫자 조합, 생성
    def dfs(num, visited):
        for i in range(len(split)):
            if visited[i]:
                continue

            visited[i] = True

            new_num = num * 10 + split[i]
            nums.add(new_num)

            dfs(new_num, visited)

            visited[i] = False

    visited = [False] * len(split)
    dfs(0, visited)
    
    # 숫자 소수 확인
    for num in nums:
        if ( check_prime(num)==True ):
            answer += 1
    
    return answer

def check_prime(k):
    if k < 2:
        return False
    for i in range(2, int(k**0.5)+1):
        if ( k%i == 0 ):
            return False
    return True