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

'''
이 문제는 row X column개의 카드에서 각 행에서 가장 작은 숫자중 비교했을때 큰 카드를 고르는 문제다.
말로만 들으면 조금 헷갈릴수도 있다. 
나는 가장 작은이라는 글씨를 보자마자 리스트의 min함수가 떠올랐다.
반복문을 이용해서 하나의 행을 받을때마다 가장 작은 숫자를 파악하고 
다른 행들과 비교해서 가장 큰 숫자를 찾았다.
답지를 보니 답지는 이중 반복문으로 문제를 풀었다. 이 문제는 카드의 개수가 10000개까지여서 이중 반복문으로 풀어도 오답 처리는 되지 않으나
카드의 개수가 많아지면 오답 처리가 될 가능성이 있다. 그러므로 나는 min 반복문으로 문제를 푸는 것을 추천한다.
'''
