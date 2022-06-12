###
# <지수> [X]

#생각했던 로직
#N을 K로 나누고 나머지값을 구한다.
#나머지값이 0이면 N을 K로 나눔.
#나머지값이 나오면 0이 될 때까지 그 수만큼 1씩 뺀다.

#나머지값이 0이 아닐 경우를 생각 못 했음.

n, k = map(int, input().split())
result = 0

n, k 
remainder = list(divmod(n, k))
  if remainder[1] = 0
    n/k
    result += 1
  else 
    remainder[1] -= 1
    result += 1

print(result)
###

###
n, k = map(int, input().split())
result = 0

while n >= k: #n이 k이상이면 k로 계속 나누기 
  while n % k !=0: #n이 k로 나누어 떨어지지 않는다면 n에서 1씩 빼기
    n -= 1
    result += 1
  n //= k #k로 나누기
  result += 1
  
 while n > 1: #남은 수에 대해 1씩 빼기
  n -= 1
  result += 1
  
print(result)
###

