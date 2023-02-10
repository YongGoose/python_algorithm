import sys
input = sys.stdin.readline

game_map = []

x,y = map(int,input().split())

d = [[0] * x for _ in range(y)]

a,b,look = map(int,input().split())

d[a][b] = 1


for i in range(y):
    maps = list(map(int,input().split()))
    game_map.append(maps)

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def turn_left():
    global look
    look -= 1
    if look == -1:
        look = 3
count = 1
turn_time = 0
while True:
    player_move_x = a - int(dx[look])
    player_move_y = b - int(dy[look])

    if d[player_move_x][player_move_y] == 0 and game_map[player_move_x][player_move_y] == 0:
        d[player_move_x][player_move_y] = 1
        # print(player_move_x,player_move_y)
        a = player_move_x
        b = player_move_y
        turn_time = 0
        count += 1
    else:
        turn_left()
        turn_time += 1
    if turn_time == 4:
        player_move_x = a - int(dx[look])
        player_move_y = b - int(dy[look])
        if game_map[player_move_x][player_move_y] == 0:
            a = player_move_x
            b = player_move_y
            turn_time = 0
        else:
            break
print(count)
    
    
