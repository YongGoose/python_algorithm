import sys
input = sys.stdin.readline

n,m = map(int,input().split())

coin_list = []
coin = [10001] * (m + 1)
for _ in range(n):
    coin_list.append(int(input()))

# coin_list.sort()

# 내가 푼 것
# if m < coin_list[0]:
#     print("-1")
# for i in range(m + 1):
#     for e in coin_list:
#         if i % e == 0:
#             coin[i] = i // e
#     if coin[i] == 0:
#         coin[i] = max(coin[i],coin[i-1] + 1)
# print(coin[m])
coin[0] = 0
for i in range(n):
    for j in range(coin_list[i], m + 1):
        if coin[j - coin_list[i]] != 10001:
            coin[j] = min(coin[j],coin[j - coin_list[i]] + 1)

if coin[m] == 10001:
    print("-1")
else:
    print(coin[m])