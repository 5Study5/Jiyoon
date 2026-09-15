from collections import deque

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)

    sum1 = sum(q1)
    sum2 = sum(q2)

    total = sum1 + sum2

    if total % 2 == 1:
        return -1

    target = total // 2
    count = 0

    max_count = (len(queue1) + len(queue2)) * 2

    while count <= max_count:
        if sum1 == target:
            return count

        if sum1 > target:
            x = q1.popleft()   # 가장 왼쪽(첫 번째) 원소 pop & 반환
            sum1 -= x
            sum2 += x
            q2.append(x)

        else:
            x = q2.popleft()
            sum2 -= x
            sum1 += x
            q1.append(x)

        count += 1

    return -1