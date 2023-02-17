import sys
input = sys.stdin.readline

n,m = map(int,input().split())

riceCake = list(map(int,input().split()))
riceCake.sort()
'''
내가 푼 방
sum = 0 
for i in range(riceCake[n - 1], 0, -1):
    for e in riceCake:
        if i < e:
            sum += e - i
            # print(sum,e,i)
    if sum == m:
        print(i)
    else:
        sum = 0
'''

start = 0
end = max(riceCake)

result = 0

while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in riceCake:
        if x > mid:
            total += x - mid
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
print(result)