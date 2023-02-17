import sys
input = sys.stdin.readline

N,M = map(int,input().split())
nums_list = []
[nums_list.append(int(input())) for _ in range(N)]
nums_list.sort()
start_index = 0
end_index = 0

result = []
while start_index < N and end_index < N:

    start = nums_list[start_index]
    end = nums_list[end_index]
    
    subtract = end - start
    if subtract == M:
        result.append(subtract)
        break
    elif subtract < M:   
        end_index += 1
    
    elif subtract > M:
        result.append(subtract)
        start_index += 1


print(min(result))
