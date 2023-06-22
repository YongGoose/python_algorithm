# |이 코드는 크루스칼 알고리즘을 이용하여 최소 신장 트리를 구하는 코드입니다.
# |
# |좋은 점:
# |- 경로 압축(Path Compression) 기법을 사용하여 find_parent 함수의 시간 복잡도를 최적화하였습니다.
# |- 간선을 비용 기준으로 오름차순으로 정렬하여 최소 비용의 간선부터 선택하도록 하였습니다.
# |- 부모 노드를 저장하는 parent 리스트를 초기화할 때, 각 노드의 부모를 자기 자신으로 설정하여 초기화하였습니다.
# |
# |나쁜 점:
# |- 입력값을 받는 부분에서 예외 처리를 하지 않았습니다. 예를 들어, 입력값이 주어지지 않았을 때 발생할 수 있는 오류를 처리하지 않았습니다.
# |- 간선을 입력받을 때, 각 노드의 번호가 1부터 시작한다는 가정을 하고 있습니다. 따라서, 노드 번호가 0부터 시작하는 경우에는 오류가 발생할 수 있습니다.
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v,e = map(int,input().split())
parent = [0] * (v + 1)

edges = []
result = 0

for i in range(1, v+ 1):
    parent[i] = i

for _ in range(e):
    a,b,cost = map(int,input().split())
    edges.append((cost,a,b))

edges.sort()

for edge in edges:
    cost, a, b = edge

    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
print(result)