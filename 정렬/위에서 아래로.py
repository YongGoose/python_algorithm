import sys
input = sys.stdin.readline

num = int(input())
array = []

for i in range(num):
    array.append(int(input()))

for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[min_index],array[i] = array[i],array[min_index]

[print(i,end=' ') for i in array]