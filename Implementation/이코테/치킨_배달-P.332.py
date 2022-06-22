###
# <기성> [X] : 로직이 틀림 ; 구현한 로직은 한 가게에서 집까지의 거리이지만, 요구사항은 집에서 가장 가까운 가게의 거리를 요구하는 것

# 집 혹은 가게를 기준으로 거리1씩 늘리면서(?) [둘러싸는 사각형] 서치하려했으나
# 가게 혹은 집의 위치를 저장하면 될듯?
#
# 집 ~ 가게 경우의 수(순열)만큼 거리 계산 (완전탐색) ; -> 다만 아래 로직은 조합의 경우의수로됐음
# 거리: '가게 기준 집' 으로 정함
# 가게 당 집까지 거리를 다 더함; 
#
# 가게 마다 거리 길이를 모아서 
# 오름차순으로 정렬 후
# m개 만큼 더함

n, m = map(int, input().split())

houses = []
stores = []

length_list_per_stores = []

for row in range(n):
    data = list(map(int, input().split()))
    for column in range(n):
        if data[column] == 1:
            houses.append((row, column))
        elif data[column] == 2:
            stores.append((row, column))

for store in stores:
    store_row, store_column = store

    length_list = []
    for house in houses:
        house_row, house_column = house

        road_length = (abs(house_row - store_row) + abs(house_column - store_column))
        length_list.append(road_length)
    sum_road_length = sum(length_list)
    # sum_road_length = 가게의 치킨거리
    # 가게 마다의 치킨거리 비교를 위해
    length_list_per_stores.append(sum_road_length)
length_list_per_stores.sort()
result = sum(length_list_per_stores[:m])
print(result)
###