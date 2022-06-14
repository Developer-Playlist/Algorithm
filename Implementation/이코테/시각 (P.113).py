###
#<지수>[X] 시, 분, 초 로직 구현을 어떻게 해야될지 감이 안 잡혔음

time = input(int())
count = 0

if i in 3:
  count += 1

###

### 정답

h = int(input())

count = 0
for i in range(h+1): #시
  for j in range(60): #분
    for k in range(60): #초
      if '3' in str(i) + str(j) + str(k):
        count += 1
    
print(count)
###
