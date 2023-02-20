import sys
input = sys.stdin.readline

num_of_food_storage = int(input())
food = [0] * 1001

food_storage = list(map(int,input().split()))
food[0] = food_storage[0]
food[1] = max(food_storage[1],food_storage[0])
for i in range(2,num_of_food_storage):
    food[i] = max(food[i -2] + food_storage[i], food[i -1])

print(food[num_of_food_storage - 1])
