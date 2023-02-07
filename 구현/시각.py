import sys
input = sys.stdin.readline

hour = int(input())
result = 0
for hours in range(hour + 1):
    for mins in range(60):
        for secs in range(60):
            res = str(hours) + str(mins) + str(secs)
            if '3' in res:
                result += 1

print(result)




