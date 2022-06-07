###
# 현지 [X] : 마음이 급해서 문제이해부터 로직까지 잘못짠듯한..
n,m = map(int, input().split())
x = list(map(int, input().split()))
count = 0

for i in range(n):
    for j in range(i, n):
        if x[i] != x[j]:
            count += 1
print(count)
###

###
# 기성 [O]
n, m = map(int, input().split())
data = list(map(int, input().split()))

memo = [0] * (m+1)
result = 0

for i in data:
    memo[i] += 1

for i in data:
    result += (sum(memo) - memo[i])
    memo[i] -= 1

print(result)
###


###
# 지수 [x] : 정답보고 간신히.. 이해. A가 선택하면 B가 선택할 수 있는 경우의 수는 줄어든 다는 것을 생각하지 못함. (중복되는 경우의 수는 피해야 하니까)

n, m = map(int, input().split())
data = list(map(int, input().split()))

weight = [0] * 11 

for x in data:
    weight[x] += 1
#공의 무게가 1부터 10까지 있음. 길이가 11인 리스트로 초기화한 후 for문을 돌면서 공이 몇 개 있는지 갯수 세서 저장

result = 0
for i in range(1, m + 1):
    n -= weight[i] #무게가 i인 A가 선택할 수 있는 경우는 제외 
    result += weight[i] * n #B가 선택하는 경우의 수와 곱하기

print(result)
###
















###
# 입력예시
# 5 3
# 1 3 2 3 2
#
# 출력예시
# 8

# 모범답안
n, m = map(int, input().split())
data = list(map(int, input().split()))

array = [0] * 11

for x in data:
    array[x] += 1

result = 0
for i in range(1, m + 1):
    n -= array[i]
    result += array[i] * n

print(result)
###
