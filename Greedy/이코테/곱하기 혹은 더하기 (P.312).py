###
# 민석 [X] : 정답처럼 첫번째 숫자를 result에 대입하는게 맞는지 그냥 1 대입하고 시작해도되는지 잘 모르겠음.
s=input()
result = 1

for i in s:
  if int(s[i]) > 1:
    result *= int(s[i])
  else:
    result += int(s[i])
    
print(result)

###

###
# 기성 [O] : 다만 하드코딩 느낌이 강하다 / 모범답안처럼 반복문 속에서 그냥 처리 가능하다 (따로 리스트를 )
nums = input()

target = []
for i in range(len(nums)):
    target.append(nums[i])

result = int(target[0])
for idx, i in enumerate(target[1:]):
    idx +=1
    if nums[idx - 1] == '0':
        result += int(i)
    elif nums[idx - 1] == '1':
        result += 0
    else:
        result *= int(i)

print(result)
###




















###
# 입력예시
# 02984
#
# 출력예시
# 576

# 모범답안
data = input()

result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result += num

print(result)
###
