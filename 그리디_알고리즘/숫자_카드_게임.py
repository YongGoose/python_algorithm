import sys
input = sys.stdin.readline
#열과 행
row,columm = map(int,input().split())
result = 0
for _ in range(row):
    card = list(map(int,input().split()))
    min_card = min(card)
    result = max(result,min_card)

print(result)

