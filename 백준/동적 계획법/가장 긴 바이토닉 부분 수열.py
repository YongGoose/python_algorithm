import bisect

x = int(input())
arr = list(map(int, input().split()))

dp = [arr[0]]

for i in range(x):
    if arr[i] > dp[-1]:
        dp.append(arr[i])
        print(arr[i],"append")
    else:
        idx = bisect.bisect_left(dp, arr[i]) # 만약에 arr[i]보다 더 작으면 증가하는 수열에서 적절한 위치를 찾은 뒤, 넣는다.
        print(dp,"idx",idx)
        dp[idx] = arr[i]

print(len(dp),dp)