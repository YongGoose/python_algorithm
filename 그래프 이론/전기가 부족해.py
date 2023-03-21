def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a == b: # a와 b가 같은 경우는 부모가 같은 경우 이므로 순환 하기때문에 신장트리에 어긋난다.
         return False
# 정점의 수보다 하나 더 큰 크기로 발전소 리스트를 만들 수도 있었지만 입력 받은 발전소만 이용해서 풀었다.
    a_p = a in p_num 
    b_p = b in p_num
    if a_p and b_p: # a_p와 b_p가 둘다 있는 경우는 발전소 두개에 연결되는 경우이므로 제외한다.
         return False
    if a_p: # 한쪽만 연결된 경우에는 연결되지 않은 쪽의 부모노드를 연결된 쪽으로 한다.
         parent[b] = a
    elif b_p: # 위와 같은 경우다.
         parent[a] = b
    else:
        if a > b: # 둘다 연결되지 않았을때는 부모의 크기로 비교해서 더 큰쪽을 부모로 한다.
             parent[b] = a
        else:
             parent[a] = b
    return True

v,e,p = map(int,input().split())
parent = [0] * (v + 1)
edges = []
result = 0

p_num = list(map(int,input().split()))

for i in range(1, v+ 1):
    parent[i] = i

for _ in range(e):
    a,b,cost = map(int,input().split())
    edges.append((cost,a,b))

edges.sort()

for edge in edges:
    cost, a, b = edge

    if find_parent(parent, a) != find_parent(parent, b):
            if union_parent(parent, a, b):
                result += cost
print(result)

