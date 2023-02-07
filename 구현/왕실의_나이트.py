import sys
input = sys.stdin.readline

mission = input()

move_type = [(-2,1),(-2,-1),(-1,-2),(-1,2),(2,1),(2,-1),(1,2),(1,-2)]
alpha = int(ord(mission[0])) - int(ord('a')) + 1 # ord함수를 사용하면 아스키코드를 이용할수 있다.
num = int(mission[1])
result = 0
for i in move_type:
    row = alpha - i[0]
    column = num - i[1]

    if row >= 1 and row <= 8 and column >= 1 and column <= 8:
        result += 1

print(result)

