import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split())
start = int(input())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
# 개선된 다익스트라 코드에서는 visited 리스트가 없다.
for _ in range(m):
    a,b,c = map(int,input().split()) # a에서 b로 가는 값이 c이다.
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        dist,now = heapq.heappop(q)

        if distance[now] < dist: # dist 보다 작으면 이미 방문했다는 뜻이다. 왜냐하면 18번째 줄에서 distance[start]의 값을 0으로 하기 때문이다.
            #또한 dist보다 큰 값도 스킵해주는 역할을 한다.
            continue
        for i in graph[now]:
            cost = dist + i[1] # 0 + i[1] -> i번째 원소로 가는 길이

            if cost < distance[i[0]]: # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우 
                #ex) 현재노드가 1번인데 2번으로 가려고 한다 이때 1번에서 3번을 가는 길이는 4이지만 2에서 3을 가는 길이는 1이고 1에서 2을 가는 길이는 1이다.
                # 그러면 4 보다 1 + 1이 더 작으므로 길이를 2로 초기화 한다.
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])