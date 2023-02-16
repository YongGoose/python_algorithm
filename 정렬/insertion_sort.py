array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)):
    for j in range(i,0,-1):
        if array[j] < array[j-1]: #오름차순으로 정리할때 앞에 있는 원소보다 뒤에 있는 원소보다 크면 위치를 바꾼다. 
            #ex 7,5이면 위치를 바꾼다.
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

print(array)