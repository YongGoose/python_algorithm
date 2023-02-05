import sys
input = sys.stdin.readline

mission_num, num = map(int,input().split())
result = 0
while True:
    if mission_num == 1:
        break
    
    elif mission_num % num == 0:
        mission_num //= num
        result += 1
    
    else:
        mission_num -= 1
        result += 1

print(result)
