import sys
input = sys.stdin.readline
mission_num = int(input())
num = [0] * 30000
time = 0
for i in range(2,mission_num + 1):
    num[i] = num[i-1] + 1
    if i % 5 == 0:
        num[i] = min(num[i // 5] + 1,num[i])
    elif i % 3 == 0:
        num[i] = min(num[i // 3] + 1,num[i])
    elif i % 2 == 0:
        num[i] = min(num[i // 2] + 1,num[i])
    
print(num[mission_num])

