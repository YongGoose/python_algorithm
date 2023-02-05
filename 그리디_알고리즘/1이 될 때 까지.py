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

'''
이 문제는 주어진 숫자를 최소한의 계산을 통하여 1로 만드는 문제다.
주어진 숫자를 두번째 숫자로 나누거나 아니면 1을 빼는 계산을 통해 1로 만들어야 한다.

나는 무한반복문을 통해 주어진 숫자가 두번째 숫자로 나눠지면 나누고 나눠지지 않는다면 1을 빼도록 했다.
답지를 확인해보니 나와 비슷하게 푼것 같다.
'''