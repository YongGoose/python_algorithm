import sys
from collections import deque
input = sys.stdin.readline

node = int(input())
line = int(input())
lines = [[False] * (node+1) for _ in range(node + 1)]
for _ in range(line):
    a,b = map(int,input().split())
    lines[a][b] = True
    lines[b][a] = True

def dfs(start,visited):
    result = 0
    visited[start] = True
    queue = deque([start])
    while queue:
        num = queue.popleft()
        for i in range(1,node + 1):
            if not visited[i] and lines[num][i]:
                visited[i] = True
                queue.append(i)
                result += 1
    return result
visited = [False] * (node + 1)
result = dfs(1,visited)
print(result)