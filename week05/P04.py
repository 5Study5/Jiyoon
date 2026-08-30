def solution(number, k):
    stack = []

    for num in number:

        while stack and k > 0 and stack[-1] < num: # 앞에 있는 숫자가 현재 숫자보다 작고(stack[-1]<num, 제거할 수 있으면(k>0) 제거
            stack.pop()
            k -= 1

        stack.append(num)

    if k > 0:
        stack = stack[:-k]  # 54321 처럼 내림차순 정렬되어 k가 안 줄어들면, 맨 뒤에서부터 k개 제거

    return ''.join(stack)