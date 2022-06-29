###
#<지수>
#선택 정렬 소스코드
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
  min_index = i #가장 작은 원소의 인덱스
  for j in range(i + 1, len(array)):
    if array[min_index] > array[j]:
      min_index = j
  array[i], array[min_index] = array[min_index], array[i] #스와프. 특정한 리스트가 주어졌을 때 두 변수의 위치를 변경하는 작업
  
print(array)

#파이썬 스와프 코드
#0 인덱스와 1 인덱스의 원소 교체하기
array = [3. 5]
array[0], array[1] = array[1], array[0]

print(array)
###
