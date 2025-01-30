#선택 정렬 소스코드
array = [7,5,9,0,3,1,6,2,4,8]
for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    #가장 앞에 있는 것과, 가장 작은 값을 스와프
    array[i], array[min_index] = array[min_index] , array[i]


print(array)

