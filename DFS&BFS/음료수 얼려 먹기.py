from collections import deque
import sys
input = sys.stdin.readline

width, height = map(int,input().split())

queue = []
for _ in range(width):
    queue.append(list(input()))
def dfs(x,y):
    if x <= -1 or y <= -1 or x >= width or y >= height:
        return False
    
    if queue[x][y] =='0':
        queue[x][y] = '1'
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False
result = 0
for i in range(width):
    for e in range(height):
        if dfs(i,e) == True:
            result += 1

print(result)

