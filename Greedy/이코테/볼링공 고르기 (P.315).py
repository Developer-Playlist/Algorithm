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
