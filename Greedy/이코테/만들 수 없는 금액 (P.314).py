###
# <기성> [X] : 로직 완전 잘못된 방향; 지금 로직은 두개만 뽑아서 더하는 연산
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 1

if data[0] != 1:
    print(result)
else:
    target = []
    target.append(result)
    for i in data:
        for j in data[1:]:
            target.append(i+j)
    target.sort()

    for idx, value in enumerate(target):
        if idx == len(target) - 1:
            result = value + 1
            break

        if target[idx + 1] - target[idx] > 1:
            result = value + 1
            break

    print(result)
###

###
# <현지> [O] : 로직 생각한 후에 구현하는데 시간을 너무 많이 씀; 0으로 시작하는것보다 1로 시작하는게 훨씬 깔끔했을것 같다.
x = int(input())
coin_list = list(map, input().split())

coin_list.sort()

cost = 0 # 만들 수 없는 금액 찾기
for coin in coin_list:
    if cost + 1 < coin:
        break
    cost += coin
print(cost + 1)
###

### 
# < 민석 > [X] : 잘 모르겠어서 답지 참고함. 
N = int(input())
coin = list(map, input().split())
coin.sort()

result = 1
for i in coin:
    if coin < i:
        break
    result += i
    
print(result)

###

### 
# <지수> [X] : 로직 잘 못 생각함. 만들수 있는 모든 금액을 다 만들고 그 금액들중에 없는 값중에 최솟값을 찾으려했음. 답안보고 이해.
n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for i in data:
    if target < i:
        break
    target += i
    
print(target)

###











###
# 입력예시
# 5
# 3 2 1 1 9
#
# 출력예시
# 8

# 모범답안
n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    if target < x:
        break
    target += x
    
print(target)
###
