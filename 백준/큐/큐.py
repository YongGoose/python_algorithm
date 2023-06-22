# |이 코드는 큐를 구현하는 문제를 해결하는 코드입니다.
# |
# |좋은 점:
# |1. deque 라이브러리를 사용하여 큐를 구현하였습니다. deque는 스택과 큐의 기능을 모두 가지고 있어서 구현이 간단하고 빠릅니다.
# |2. 함수를 사용하여 각각의 명령어를 처리하였습니다. 이렇게 하면 코드의 가독성이 좋아지고 유지보수가 용이해집니다.
# |
# |나쁜 점:
# |1. isqueue() 함수를 사용하여 큐가 비어있는지 확인하는 부분이 있습니다. 이 함수는 큐의 길이를 확인하는 것과 같은 역할을 하므로, 굳이 함수를 사용하지 않고 바로 len(queue) > 0 으로 확인하는 것이 더 간단합니다.
# |2. push() 함수에서 num을 인자로 받는데, 이때 num이 문자열 형태로 들어오므로, 큐에는 문자열 형태로 저장됩니다. 이는 나중에 문제를 해결할 때 불편함을 초래할 수 있으므로, int(num)으로 형변환을 해주는 것이 좋습니다.
# |
'''
push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''
from collections import deque
import sys
input = sys.stdin.readline
queue = deque()
def isqueue():
    if len(queue) > 0:
        return True
    else:
        return False

def push(num):
    queue.append(num)

def pop():
    if isqueue():
        num = queue.popleft()
        return num
    else:
        return -1

def size():
    return len(queue)

def empty():
    if isqueue():
        return 0
    else:
        return 1
def front():
    if isqueue():
        return queue[0]
    else:
        return -1
def back():
    if isqueue():
        return queue[-1]
    else:
        return -1

mission_num = int(input())
for _ in range(mission_num):
    mission = list(map(str,input().split()))
    if mission[0] == 'push':
        push(mission[1])
    
    elif mission[0] == 'pop':
        print(pop())
    
    elif mission[0] == 'size':
        print(size())

    elif mission[0] == 'empty':
        print(empty())

    elif mission[0] == 'front':
        print(front())

    elif mission[0] == 'back':
        print(back())
