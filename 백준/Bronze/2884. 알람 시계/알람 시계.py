h,m = map(int,input().split())
result = h*60 + m - 45

ch = (result // 60) % 24
cm = result % 60

print(ch, cm)
