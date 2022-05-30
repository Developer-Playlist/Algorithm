###
# <기성 1> [x] : 로직이 이상함
from collections import deque

n = int(input())
traveler = list(map(int, input().split()))

traveler.sort()
traveler = deque(traveler)

all_group = []

while traveler: # 공포도 제일 높은 여행자 고르고 그 수에 맞게 배치
    target = traveler.pop()
    group = []
    for _ in range(target-1):
        group.append(traveler.popleft())
    group.append(target)
    all_group.append(group)

print(len(all_group))

# <기성 2> 답지 참고
n = int(input())
travelers_fearness = list(map(int, input().split()))

travelers_fearness.sort()

max_group = 0
count = 0

for traveler_fearness in travelers_fearness:
    count += 1
    if traveler_fearness <= count:
        max_group += 1
        count = 0

print(max_group)
###

###
# <민석> [O] 
N = int(input())
adventurer = list(map(int, input().split()))
adventurer.sort()

group = 0
count = 0

for i in adventurer:
  count += 1
  if adventurer > count:
    group += 1
    count = 0

print(group)
###

### 
# <지수> [X]
n = int(input()) 
adventurer = list(map(int, input().split())) 
adventurer.sort() 

group = 0
count = 0

for i in adventurer:
  count += 1
  if count >= i:
    group += 1
    count = 0 #다음 그룹을 위해 모험가 수 초기화

print(group)
###


















###
# 입력예시
# 5
# 2 3 1 2 2
#
# 출력예시
# 2

# 모범답안
n = int(input())
data = list(map(int, input().split()))

data.sort()

result = 0
count = 0

for i in data:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)
###
