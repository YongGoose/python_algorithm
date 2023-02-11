def dfs(graph, v, visited):
    visited[v] = True # 입력 받은 매개변수 값을 visited에서 True로 바꾼다. 방문했다는 뜻
    print(v,end=' ')
    for i in graph[v]: # v와 연결 되어있는 인자들을 반복문으로 반복한다.
        if not visited[i]: # i가 false일때
            dfs(graph,i,visited) # 재귀함수를 이용해 반복한다.
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
dfs(graph,1,visited)
