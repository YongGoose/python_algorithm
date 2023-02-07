import sys
input = sys.stdin.readline

num = int(input())
for _ in range(num):
    floor,rooms,visitor = map(int,input().split())
    first = visitor // floor + 1
    second = visitor % floor
    if visitor % floor == 0:
        first = visitor // floor
        second = floor
    result = second * 100 + first
    print(result)