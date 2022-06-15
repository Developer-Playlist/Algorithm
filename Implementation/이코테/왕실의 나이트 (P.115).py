###
#<지수>[X] 이동할 수 있는 방향을 정의 하는 방법 말고 다른 방법이 있을 거라고 생각했는데에...일단 현재 위치 확인하는 것도 여려웠다...

input = input()
row = int(input[1])
column = int(input[0])

moves = [(-2, -1), (-2, 1), (2, -1), (2, 1), (1, -2),(1, 2), (-1, -2), (-1, 2)}
       
for move in moves:

         
###

### 정답
input_data = input()
row = int(intput_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)] #나이트가 이동할 수 있는 8가지방향

#8가지 방향에 대해 각 위치로 이동 가능한지 확인
result = 0
for step in steps:
  next_row = row + step[0]
  next_column = column + step[1]
  #해당 위치로 이동 가능하면 카운트 증가
  if next_row >= 1 and next_romw <= 8 and next_colum >= 1 and next_column <= 8:
    result += 1
    
print(result)

###
