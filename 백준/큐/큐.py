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
