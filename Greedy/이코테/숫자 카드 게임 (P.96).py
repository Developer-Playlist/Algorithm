###
# <지수> [X]

#min함수 
n, m = map(int, input().split)

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_num = min(data) #현재 줄에서 가장 작은 수 찾기
    result = max(result, min_num) #가장 작은 수들 중에서 가장 큰 수 찾기 

print(result)


#이중 포문
n, m = map(int(input().split()))

result = 0
for i in range(n):
    data = list(map(int, input().split))

    min_num = 10001 
    for a in data:
        min_num = min(min_num, a) # 현재 줄에서 가장 작은 수 찾기
    result = max(result, min_num)
print(result)

###
