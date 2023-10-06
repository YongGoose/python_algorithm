import sys

input = sys.stdin.readline
result = 0
count = 1
while True:
    L,P,V=map(int,sys.stdin.readline().split())

    if L + P + V == 0:
        break

    if V%P<=L:
        result = V // P * L + V % P
        print("Case " + str(count) + ": " + str(result))
        count += 1
    else:
        result = V // P * L + L
        print("Case " + str(count) + ": " +str(result))
        count += 1