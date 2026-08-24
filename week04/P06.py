def solution(diffs, times, limit):
    left = 1
    right = max(diffs)

    answer = right

    while left <= right:
        level = (left + right) // 2

        total = 0

        for i in range(len(diffs)):
            diff = diffs[i]
            time_cur = times[i]

            if i == 0:
                time_prev = 0
            else:
                time_prev = times[i - 1]

            if diff <= level:
                total += time_cur

            else:
                fail = diff - level
                total += fail * (time_cur + time_prev) + time_cur

            if total > limit:
                break

        if total <= limit:
            answer = level
            right = level - 1

        else:
            left = level + 1

    return answer