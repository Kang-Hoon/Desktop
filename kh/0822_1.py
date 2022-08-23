# Date : Aug 22nd
# Author : Kanghoon Lee
# 에너지 절약을 위한 최적의 엘레베이터 사용
# 더 가까운 엘레베이터가 도착하는 코드
# 
# 조건?
# 1. 같은 층이면 1번 엘레베이터가 우선적으로 도착한다
# 2. 에너지 절약을 위해서, 탑승객의 현재 층과 엘리베이터의 현재 층 차이가 같을 경우
#   2.1 위에 있는 엘리베이터가 내려오는 것을 우선으로 한다. 
#
# 입력 :
# 1) 현재 층 입력
# 2) 두 개의 리스트 (두 엘리베이터가 각각 위치한 층들의 리스트)
# 
# 출력 :
# 엘리베이터가 각각 사용된 횟수
# #

currentEl1 = list()
currentEl2 = list()

count1 = 0
count2 = 0

currentEl1 = [0,1,2,3,4,5,3,5]
currentEl2 = [1,2,3,4,5,0,3,1]

a = int(input("현재 층을 입력하세요 : "))

for i in range(len(currentEl1)):
    print("당신은 지금 ", a, "층에 있습니다.\n")
    print("1번 엘리베이터는 ", currentEl1[i], "층에 있습니다." )
    print("2번 엘리베이터는 ", currentEl2[i], "층에 있습니다." )

    if (abs(a-currentEl1[i]) < (a-currentEl2[i])) :
        print("1번 엘리베이터가 열립니다.")
        
    elif(abs(a-currentEl1[i]) > (a-currentEl2[i])):
        print("2번 엘리베이터가 열립니다.")
        count2 += 1
    elif (abs(a-currentEl1[i]) == (a-currentEl2[i])):
        if (currentEl1[i] > currentEl2[i]):
            print("1번 엘리베이터가 열립니다.")
            count1 += 1
        elif (currentEl1[i] < currentEl2[i]):
            print("2번 엘리베이터가 열립니다.")
            count2 += 1
        elif (currentEl1[i] == currentEl2[i]):
            print("1번 엘리베이터가 열립니다.")
            count1 += 1
    print()
    print("1번 엘리베이터는 ",count1, "번 열렸습니다")
    print("2번 엘리베이터는 ",count2, "번 열렸습니다")
    print()
    print()

