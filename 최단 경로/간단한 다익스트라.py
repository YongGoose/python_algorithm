import sys
input = sys.stdin.readline

INF = int(1e9)

n,m = map(int,input().split())
start = int(input())

graph = [[] for i in range(n + 1)] # 각 노드에 연결되어있는 노드에 대한 정보를 담는 리스트를 만들기
visited = [False] * (n + 1) # 방문한 적이 있는지 체크하는 리스트
distance = [INF] * (n + 1) #최단 거리 테이블을 모두 무한으로 초기화

for _ in range(m):
    a,b,c = map(int,input().split())
    #a에서 b로 가는 비용이 c라는 의미
    graph[a].append((b,c))

def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1,n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijstra(start):
    distance[start] = 0
    visited[start] = True
    
    for j in graph[start]:
        distance[j[0]] = j[1] # 숫자를 입력할때 a,b,c를 입력했는데 이때 a가 j[0]이고 b가 j[1]이다.
        #거리는 a에서 b로 가는것이므로 b의 좌표가 거리다.
    
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]

            if cost < distance[j[0]]:
                distance[j[0]] = cost
dijstra[start]

for i in range(1,n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
