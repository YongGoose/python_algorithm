import sys
input = sys.stdin.readline

num = int(input())
student = []
for _ in range(num):
    input_data = input().split()
    student.append((input_data[0], int(input_data[1])))

array = sorted(student,key=lambda student:student[1])
for i in array:
    print(i[0],end=' ')
