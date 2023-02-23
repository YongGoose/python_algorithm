import sys
input = sys.stdin.readline

stair_nums = int(input())
stair = [0] * 300
for i in range(stair_nums):
    stair[i] = int(input())

ans = [0] * (stair_nums + 301)
ans[0] = stair[0]
ans[1] = stair[1] + stair[0]
ans[2] = max(stair[0] + stair[2], stair[1] + stair[2])
for i in range(3,stair_nums):
    ans[i] = max(ans[i-3] + stair[i-1] + stair[i], ans[i-2] + stair[i])


print(ans[stair_nums-1])
