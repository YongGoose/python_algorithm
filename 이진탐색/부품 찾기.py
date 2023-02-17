import sys
input = sys.stdin.readline

n = int(input())
market_list = list(map(int,input().split()))

m = int(input())
visit_list = list(map(int,input().split()))
market_list.sort()
def binary_search(start,end,target,array):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return "yes"
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return "no"

for i in visit_list:
    if binary_search(0,n-1,i,market_list) == "yes":
        print("yes",end=" ")
    else:
        print("no", end=" ")