###
# <지수> [X]
n = 1260
count = 0

#큰 단위 화폐부터 차례대로 확인
coin_types = [500, 100, 50, 10]

for coin in coin_types:
  count += n // coin #해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
  n %= coin #거슬러줘야 하는 금액 
 
print(count)

###

###
<민석> [O]
N = int(input())
count = 0

coins = [500, 100, 50, 10]

for coin in coins:
  count += N // coin
  N %= coin
  
print(count)
###

###
# <현지> [X]
n = int(input())
count = 0

coins = [500, 100, 50, 10]

for coin in coins:
    count += n // coin
    n %= coin

print(count)
###
