from collections import deque

num, times = map(int, input().split())
num_list = deque([(i+1) for i in range(num)])

mission_list = list(map(int, input().split()))

count = 0
change_num, index, middle_number = 0, 0, num // 2

for i in range(times):
    for j in range(num):
        if num_list[j] == mission_list[i]:
            index = j
    
    # 덱의 중간 위치를 기준으로 이동 방향을 결정합니다.
    if middle_number >= index:
        while num_list[0] != mission_list[i]:
            change_num = num_list.popleft()
            num_list.append(change_num)
            count += 1
    else:
        while num_list[0] != mission_list[i]:        
            change_num = num_list.pop()
            num_list.appendleft(change_num)
            count += 1
        
    if num_list[0] == mission_list[i]:
        num_list.popleft()
        num -= 1
        middle_number = num // 2

print(count)
