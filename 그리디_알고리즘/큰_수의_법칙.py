# 내가 푼 것
import sys

input = sys.stdin.readline

N,M,K = map(int,input().split())
nums_list = list(map(int,input().split()))
nums_list.sort(reverse=True)

first = nums_list[0]
second = nums_list[1]

sum = 0
while True:
    if M == 0:
        break
    for _ in range(K):
        sum += first
        M -= 1
        if M == 0:
            break
    sum += second
    M -= 1
print(sum)

# 문제 답안
n,m,k = map(int,input().split())
data = list(map(int,input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

count = int(m / (k + 1)) * K
count += m % (k + 1)

result = 0
result += count * first
result += (m-count) * second

print(result)


'''
이 문제는 n개의 숫자를 M번 더하여 가장 큰수를 만드는 문제다.
특이한 규칙이 하나 있는데 바로 K번 이상 더할수 없다는 것이다.

나는 문제를 보자마자 무한반복문을 이용해서 숫자를 더할 생각을 했다.
하지만 답지(?)를 보니 내가 풀었던 방법은 빅오 표기법으로 하면 O(N)의 시간복잡도를 가지고 있었다.
그러므로 m의 개수가 일정 숫자 이상 커지면 실행시키는데 1초 이상 걸리게 돼서 오답처리가 될 가능성이 있다.

답지는 가장 큰 수를 더할 횟수를 구하고 나머지 횟수로 두번째 숫자를 더하는 방식으로 풀었다.
이렇게 하면 복잡도가 훨씬 줄어들것 같다는 생각이 든다.
다음에 Greedy algorithm 문제를 보면 한번 더 생각을 하고 풀자.
'''