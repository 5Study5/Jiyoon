def solution(storey):
    answer = 0

    while storey > 0:
        digit = storey % 10

        if digit > 5:
            answer += 10 - digit
            storey += 10 - digit

        elif digit < 5:
            answer += digit

        else:  # digit == 5
            next_digit = (storey // 10) % 10

            if next_digit >= 5:
                answer += 5
                storey += 5
            else:
                answer += 5

        storey //= 10

    return answer