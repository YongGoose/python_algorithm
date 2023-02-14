from collections import deque
import sys
input = sys.stdin.readline

width, height = map(int,input().split())
game_map = [[0] * (height) for _ in range(width)]
maze_map = []

for _ in range(width):
    maze_map.append(list(input()))
dx = [-1,1,0,0]
dy = [0,0,1,-1]
for i in range(width):
    for e in range(height):
        if maze_map[i][e] == '\n':
            continue
        else:
            game_map[i][e] = int(maze_map[i][e])
def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= width or ny >= height:
                continue
            if game_map[nx][ny] == 0:
                continue
            if game_map[nx][ny] == 1:
                queue.append((nx,ny))
                game_map[nx][ny] = game_map[x][y] + 1
    return game_map[width-1][height-1]

print(bfs(0,0))
