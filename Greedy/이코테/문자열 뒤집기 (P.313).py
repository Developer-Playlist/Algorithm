###
# <기성> [O]
data = input()

zero_group = 0
one_group  = 0

for idx, value in enumerate(data):
    if idx == len(data) - 1:
        if value == '0':
            zero_group += 1
        if value == '1':
            one_group += 1
        break

    if value != data[idx + 1]:
        if value == '0':
            zero_group += 1
        if value == '1':
            one_group += 1

result = min(zero_group, one_group)
print(result)
###

###
# <민석> [0]
S = input()

result = 0

for i in range(1, len(S)):
  if S[i-1] != S[i]:
    result += 1

print(result-1)
###

###
# <현지> [X]
# 1. 0과1중에 반복횟수가 적은것을 min_num 변수에 저장 (문자열이 0과1로만 이루어져있기 때문에 가능)
# 2. 하나씩 보면서 min_num과 같으면 바꿔주고, count를 하나 늘리기
# 문제점 1. 반복횟수를 구하면서 list로 바꾸는게 너무 비효율적이다 -> least repeating number 구하는 좋은 방법 없을까?
# 문제점 2. 연속된 숫자를 바꿀때 한번의 count로 행하는데 이걸 구현하지 못했다. 

S = input()
S_list = list(S)
min_num = min(S_list, key=S_list.count) #0과 1중에 더 적은걸 찾기

count = 0
for i in range(len(S)):
    if S[i] == min_num:
        S[i] == 1-int(min_num)
        count += 1
    if count == len(S):
        count = 0
print(count)
###

### 
#<지수> [X]
#0이 되는 경우와 1이 되는 경우 중 더 적게 변환하는 값을 찾기
#첫번째 이후 값은 어떻게 구하는 지 모르겠음... 정답보고 이해

i = input()

zero = 0
one = 0

if i[0] == '1':
    zero += 1
else:
    one += 1
   

print(min(zero, one))

###






###
# 입력예시
# 0001100
#
# 출력예시
# 1

# 모범답안
data = input()
count0 = 0
count1 = 0

if data[0] == '1':
    count0 += 1
else:
    count1 += 1

for i in range(len(data) - 1):
    if data[i] != data[i + 1]:
        if data[i + 1] == '1':
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1))
###
