def solution(numbers, target):
    answer = 0
    
    def dfs(index, total):
        nonlocal answer    # 바깥의 solution 함수의 answer 변수 사용을 위해.

        # 모든 숫자를 다 사용한 경우
        if index == len(numbers):
            if total == target:
                answer += 1
            return

        # 현재 숫자를 더하는 경우
        dfs(index + 1, total + numbers[index])

        # 현재 숫자를 빼는 경우
        dfs(index + 1, total - numbers[index])

    dfs(0, 0)
    
    return answer