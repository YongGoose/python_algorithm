from collections import deque # popleft를 사용하기 위해 덱 모듈을 가져온다.

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue: # queue가 공백이 될때까지 진행하는 while 반복문이다.
        v = queue.popleft() # queue의 맨 앞에 있는 인자를 빼낸다.
        print(v,end=' ')

        for i in graph[v]: # v와 접촉한 인자들을 for 반복문을 이용하여 반복시킨다.
            if not visited[i]: # 만약 visited 값이 false라면 
                queue.append(i) # queue에 i값을 넣는다.
                visited[i] = True # 그 후, i를 True로 바꾼다.

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visited = [False] * 9
bfs(graph,1,visited)