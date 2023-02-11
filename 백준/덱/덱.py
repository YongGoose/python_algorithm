import sys
from collections import deque
input = sys.stdin.readline

mission_num = int(input())
mission_deque = deque(list())
def push_front(x):
    mission_deque.appendleft(x)

def push_back(x):
    mission_deque.append(x)
def empty():
    if len(mission_deque) == 0:
        return 1
    else:
        return 0
def pop_front():
    if empty() == 1:
        return -1
    else:
        num = mission_deque.popleft()
        return num
def pop_back():
    if empty() == 1:
        return -1
    else:
        num = mission_deque.pop()
        return num
def size():
    return len(mission_deque)
def front():
    if empty() == 1:
        return -1
    else:
        return mission_deque[0]
def back():
    if empty() == 1:
        return -1
    else:
        return mission_deque[-1]

for _ in range(mission_num):
    mission = list(map(str,input().split()))

    if mission[0] == 'push_front':
        push_front(mission[1])
    elif mission[0] == 'push_back':
        push_back(mission[1])
    elif mission[0] == 'empty':
        print(empty())
    elif mission[0] == 'pop_front':
        print(pop_front())
    elif mission[0] == 'pop_back':
        print(pop_back())
    elif mission[0] == 'size':
        print(size())
    elif mission[0] == 'front':
        print(front())
    elif mission[0] == 'back':
        print(back())