import sys
input = sys.stdin.readline

ans = [[[0]*(21) for _ in range(21)] for _ in range(21)]

def happy_recursion(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    elif a > 20 or b > 20 or c > 20:
        return happy_recursion(20,20,20)

    if ans[a][b][c]:
        return ans[a][b][c]   

    elif a < b and b < c:
        ans[a][b][c] = happy_recursion(a,b,c-1) + happy_recursion(a,b-1,c-1) - happy_recursion(a,b-1,c)
        return ans[a][b][c]
    
    else:
        ans[a][b][c] = happy_recursion(a-1,b,c) + happy_recursion(a-1,b-1,c) + happy_recursion(a-1,b,c-1) - happy_recursion(a-1,b-1,c-1)
        return ans[a][b][c]

while True:
    a,b,c = map(int,input().split())

    if a == -1 and b == -1 and c == -1:
        break
    else:
        print("w({}, {}, {}) = {}".format(a,b,c,happy_recursion(a,b,c)))



