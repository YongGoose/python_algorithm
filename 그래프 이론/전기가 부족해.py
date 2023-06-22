# |이 코드는 최소 스패닝 트리(Minimum Spanning Tree)를 구하는 Kruskal 알고리즘을 이용하여 문제를 해결하는 코드입니다.
# |
# |좋은 점:
# |- 경로 압축(Path Compression) 기법을 사용하여 부모 노드를 찾는 함수를 최적화하였습니다. 이를 통해 시간 복잡도를 줄일 수 있습니다.
# |- 발전소 노드인지 아닌지를 판별하여, 발전소 노드끼리는 연결하지 않도록 하였습니다. 이를 통해 문제의 조건을 만족시키며, 최소 스패닝 트리를 구할 수 있습니다.
# |
# |나쁜 점:
# |- 코드의 가독성이 떨어집니다. 함수의 이름이나 변수명이 간결하지 않아, 코드를 이해하기 어려울 수 있습니다.
# |- 발전소 노드인지 아닌지를 판별하는 부분에서, 발전소 노드 리스트를 매번 확인해야 합니다. 이를 개선하기 위해서는 발전소 노드 리스트를 미리 정렬하여 이진 탐색(Binary Search)을 이용하는 방법이 있습니다.
# |
# 부모 노드를 찾는 함수
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
    def find_parent(parent, x):
        if parent[x] != x:  # 부모 노드가 자기 자신이 아닌 경우, 부모 노드를 찾기 위해 재귀 호출
            # 경로 압축(Path Compression) 기법을 사용하여 부모 노드를 찾음
            parent[x] = find_parent(parent, parent[x])
        return parent[x]

    # 두 노드를 연결하는 함수


    def union_parent(parent, a, b):
        a = find_parent(parent, a)  # a의 부모 노드를 찾음
        b = find_parent(parent, b)  # b의 부모 노드를 찾음
        if a == b:  # a와 b가 같은 부모 노드를 가지고 있는 경우, 순환을 발생시키므로 False 반환
            return False
        # 발전소 리스트에 속한 노드인지 확인
        a_p = a in p_num
        b_p = b in p_num
        if a_p and b_p:  # a와 b가 모두 발전소 노드인 경우, False 반환
            return False
        if a_p:  # a만 발전소 노드인 경우, b의 부모 노드를 a로 설정
            parent[b] = a
        elif b_p:  # b만 발전소 노드인 경우, a의 부모 노드를 b로 설정
            parent[a] = b
        else:  # a와 b가 모두 발전소 노드가 아닌 경우, 두 노드 중 부모 노드의 크기가 더 큰 쪽을 부모로 설정
            if a > b:
                parent[b] = a
            else:
                parent[a] = b
        return True


    # 입력 받기
    v, e, p = map(int, input().split())  # 노드 수, 간선 수, 발전소 수
    parent = [0] * (v + 1)  # 부모 노드 리스트 초기화
    edges = []  # 간선 리스트 초기화
    result = 0  # 최소 비용 초기화

    p_num = list(map(int, input().split()))  # 발전소 노드 리스트 입력 받기

    for i in range(1, v + 1):
        parent[i] = i  # 부모 노드 리스트 초기화

    for _ in range(e):
        a, b, cost = map(int, input().split())  # 노드 a와 노드 b를 연결하는 비용 cost 입력 받기
        edges.append((cost, a, b))  # 간선 리스트에 추가

    edges.sort()  # 비용이 적은 순서대로 간선 리스트 정렬

    for edge in edges:
        cost, a, b = edge  # 비용, 노드 a, 노드 b

        if find_parent(parent, a) != find_parent(parent, b):  # 노드 a와 노드 b가 서로 다른 부모 노드를 가지고 있는 경우
            if union_parent(parent, a, b):  # 두 노드를 연결하고, 순환을 발생시키지 않는 경우
                result += cost  # 최소 비용에 비용 추가

    print(result)  # 최소 비용 출력