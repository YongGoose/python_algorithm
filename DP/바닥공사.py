import sys
input = sys.stdin.readline

tile = [0] * 1001
nums_of_tile = int(input())
tile[1] = 1
tile[2] = 3
for i in range(3,nums_of_tile + 1):
    tile[i] = tile[i-2] * 2 + tile[i-1]
print(tile[nums_of_tile])