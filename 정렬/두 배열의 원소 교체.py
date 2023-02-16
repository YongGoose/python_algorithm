import sys
input = sys.stdin.readline

n,k = map(int,input().split())

array_a = (list(map(int,input().split())))
array_b = (list(map(int,input().split())))


def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]
    
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

a = quick_sort(array_a)
b = quick_sort(array_b)

for _ in range(k):
    a.append(b.pop(n-1))
    b.append(a.pop(0))
    a = quick_sort(a)
    b = quick_sort(b)

sum = 0

for i in range(n):
    sum += a[i]
print(sum)

