import sys
input = sys.stdin.readline

N,S = map(int,input().split())
nums_list = list(map(int,input().split()))

start_index = 0
end_index = 0
sum = 0
min_length = sys.maxsize
while True:
    if sum >= S:
        min_length = min(min_length,end_index - start_index)
        sum -= nums_list[start_index]
        start_index += 1
    elif end_index == N:
        break
    else:
        sum += nums_list[end_index]
        end_index += 1

if min_length == sys.maxsize:
    print("0")
else:
    print(min_length)

