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
