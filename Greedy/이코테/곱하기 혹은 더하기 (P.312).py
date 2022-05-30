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
