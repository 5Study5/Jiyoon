# 최소 신장트리 (MST)
def solution(n, costs):
    answer = 0

    # 부모 노드 초기화
    parent = [i for i in range(n)]
    count = 0

    # 비용이 작은 순서대로 정렬
    costs.sort(key=lambda x: x[2])  # lambda는 이름 없는 짧은 함수를 만드는 문법 =>  lambda 매개변수: 반환값

    for a, b, cost in costs:
         # 서로 다른 집합에 있다면 연결, 같은 그룹이면 건너뜀(사이클 생성x)
        if find(parent, a) != find(parent, b):
            union(parent, a, b)

            answer += cost
            count += 1

            if count == n - 1:    # 모든 섬 n개를 연결하는 데 필요한 다리 개수는 항상 n-1개. n-1 개 되면 종료.
                break

    return answer

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])

    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b