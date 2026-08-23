# 정렬 후 비교
def solution(participant, completion):
    
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]

    return participant[-1]

# 반복문 풀이 (시간 초과)
def solution(participant, completion):

    copy = participant.copy()
    
    for name in completion:
        copy.remove(name)
    
    return copy[0]