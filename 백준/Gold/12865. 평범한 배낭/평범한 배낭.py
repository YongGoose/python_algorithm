n, k = map(int, input().split())  # n: 물품의 수, k: 가방에 넣을 수 있는 최대 무게
dp = [[0] * (k+1) for _ in range(n+1)]
m = [[0, 0]]
for i in range(n):
    w, v = map(int, input().split())  # w: 각 물건의 무게, v: 물건의 가치
    m.append([w, v])

for i in range(1, n+1):
    w = m[i][0] # 무게
    v = m[i][1] # 가치
    for j in range(1, k+1):
        if j < w: #1부터 최대 무게까지 반복하는 반복문과 무게를 비교해서 무게가 더 높으면
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-w] + v, dp[i-1][j])
print(dp[n][k])