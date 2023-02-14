import sys
from collections import deque
input = sys.stdin.readline

length = int(input())
apt = []
apt_map = [[0] * length for _ in range(length)]

for _ in range(length):
    apt.append(list(input()))
for i in range(length):
    for e in range(length):
        apt_map[i][e] = int(apt[i][e])
# print(apt_map)
visited = [[False] * (length) for _ in range(length)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y,visited):
    apt_size = 1
    if apt_map[x][y] == 1 and not visited[x][y]:
        visited[x][y] = True
        queue = deque([(x,y)])
        while queue:
            q,w = queue.popleft()
            for i in range(4):
                nx = q + dx[i]
                ny = w + dy[i]

                if nx < 0 or ny < 0 or ny >= length or nx >= length:
                    continue
                if visited[nx][ny] == True or apt_map[nx][ny] == 0:
                    continue
                queue.append((nx,ny))
                visited[nx][ny] = True
                apt_size += 1
        return apt_size
size = 0
apt_result = []
for i in range(length):
    for e in range(length): 
        result = bfs(i,e,visited)
        if result is not None:
            size += 1
            apt_result.append(result)
apt_result.sort()
print(size)
for i in range(size):
    print(apt_result[i])


