def solution(people, limit):
    people.sort()

    left = 0
    right = len(people) - 1

    answer = 0

    while left <= right:

        # 한 명만 남은 경우
        if left == right:
            answer += 1
            break

        # 가장 가벼운 사람 + 가장 무거운 사람이 같이 탈 수 있으면
        if people[left] + people[right] <= limit:
            left += 1
            right -= 1

        # 같이 못 타면 가장 무거운 사람 혼자 탐
        else:
            right -= 1

        answer += 1

    return answer