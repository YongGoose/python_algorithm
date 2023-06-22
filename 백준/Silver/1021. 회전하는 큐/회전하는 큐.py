from collections import deque
import sys

input = sys.stdin.readline

num, times = map(int,input().split())
num_list = deque([(i+1) for i in range(num)])

mission_list = list(map(int,input().split()))

count = 0
change_num, index, middle_number = 0,0, num // 2

for i in range(times):
    for e in range(num):
        if(num_list[e] == mission_list[i]):
            index = e
    if(middle_number >= index):
        while (num_list[0] != mission_list[i]):
            change_num = num_list.popleft()
            num_list.append(change_num)
            count += 1
    else:
        while (num_list[0] != mission_list[i]):        
            change_num = num_list.pop()
            num_list.appendleft(change_num)
            count += 1
        
    if(num_list[0] == mission_list[i]):
        num_list.popleft()
        num -= 1
        middle_number = num // 2

print(count)
        