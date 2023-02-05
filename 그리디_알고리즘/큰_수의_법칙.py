# 내가 푼 것
import sys

input = sys.stdin.readline

N,M,K = map(int,input().split())
nums_list = list(map(int,input().split()))
nums_list.sort(reverse=True)

first = nums_list[0]
second = nums_list[1]

sum = 0
while True:
    if M == 0:
        break
    for _ in range(K):
        sum += first
        M -= 1
        if M == 0:
            break
    sum += second
    M -= 1
print(sum)

# 문제 답안
# n,m,k = map(int,input().split())
# data = list(map(int,input().split()))

# data.sort()
# first = data[n-1]
# second = data[n-2]

# count = int(m / (k + 1)) * K
# count += m % (k + 1)

# result = 0
# result += count * first
# result += (m-count) * second

# print(result)