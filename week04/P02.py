
from collections import defaultdict
from bisect import bisect_left


def solution(info, query):
    answer = []
    data = defaultdict(list)

    # 1. 지원자 정보를 16가지 조건으로 저장
    for person in info:
        temp = person.split()

        conditions = temp[:4]
        score = int(temp[4])

        for mask in range(16):
            key = ""

            for i in range(4):
                if mask & (1 << i):
                    key += "-"
                else:
                    key += conditions[i]

            data[key].append(score)

    # 2. 각 조건에 저장된 점수 정렬
    for key in data:
        data[key].sort()

    # 3. query 처리
    for q in query:
        q = q.replace(" and ", " ").split()

        key = "".join(q[:4])
        score = int(q[4])

        scores = data[key]

        # score 이상이 처음 등장하는 위치
        index = bisect_left(scores, score)

        # index부터 끝까지의 개수
        answer.append(len(scores) - index)

    return answer






# ======================================================================================================

# 시간 초과 - 실패

def solution(info, query):
    answer = []

    converted_info = convert(info)
    converted_query = convert(query)

    for i in range(len(query)):
        n = 0        # query 충족하는 사람 수

        for j in range(len(info)):
            matched = True

            for k in range(4):
                # query가 -가 아니면서 서로 다르면 조건 불일치
                if converted_query[i][k] != -1:
                    if converted_info[j][k] != converted_query[i][k]:
                        matched = False
                        break

            if matched:
                if converted_info[j][4] >= converted_query[i][4]:
                    n += 1

        answer.append(n)

    return answer


def convert(arr):
    lang = ["cpp", "java", "python"]
    part = ["backend", "frontend"]
    career = ["junior", "senior"]
    soul_food = ["chicken", "pizza"]

    all_info = [lang, part, career, soul_food]

    converted = []    # 전체

    for i in range(len(arr)):
        temp = []     # 한 줄

        line = arr[i].replace(" and ", " ").split()

        for j in range(4):
            if line[j] == "-":
                temp.append(-1)
            else:
                index = all_info[j].index(line[j])
                temp.append(index)

        temp.append(int(line[4]))   # score

        converted.append(temp)

    return converted