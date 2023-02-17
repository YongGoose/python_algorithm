num = int(input())
classroom = []

for i in range(num):
    input_data = input().split()
    classroom.append((int(input_data[0]), int(input_data[1])))

classroom = sorted(classroom,key=lambda classroom : classroom[0])
classroom = sorted(classroom,key=lambda classroom : classroom[1])

# print(classroom,"\n")
num_of_class = 0

end = 0
for i in classroom:
    if i[0] >= end or num_of_class == 0:
        end = i[1]
        # print(i)
        num_of_class += 1

print(num_of_class)