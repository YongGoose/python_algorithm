import sys
input = sys.stdin.readline

house_num = int(input())
house_RGB = []
for _ in range(house_num):
    house_RGB.append(list(map(int,input().split())))
ans = [[0] * 3 for _ in range(house_num + 1)]

a = 0
for i in range(1, house_num + 1):
    ans[i][0] = min(ans[i-1][1],ans[i-1][2]) + house_RGB[i-1][0]
    ans[i][1] = min(ans[i-1][0],ans[i-1][2]) + house_RGB[i-1][1]
    ans[i][2] = min(ans[i-1][0],ans[i-1][1]) + house_RGB[i-1][2]

print(min(ans[house_num][0],ans[house_num][1],ans[house_num][2]))


