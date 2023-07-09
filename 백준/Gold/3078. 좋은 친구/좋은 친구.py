from sys import stdin
# from collections import deque
n,k = map(int, stdin.readline().split())
student = [0]*n
num = [0]*21
count = 0

for i in range(n):
    student[i] = len(stdin.readline().rstrip())
    if i > k: # k는 친구 가능한 성적 차
        num[student[i-k-1]]-=1
    count += num[student[i]]
    num[student[i]] += 1

print(count)