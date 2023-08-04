# 떡볶이 떡 만들기
# 원하는 조건을 만족하는 가장 알맞은 값을 선택 -> 파라메트릭 서치 -> 이진 탐색
import sys

n,m = map(int,sys.stdin.readline().rstrip().split(' '))

riceCake = list(map(int,sys.stdin.readline().rstrip().split(' ')))

riceCake.sort()
result = 0
first = riceCake[0]
last = riceCake[-1]

def cutting(dMid):
    adds  = 0 
    for i in riceCake:
        if(i-dMid>=0):
            adds += i - dMid
    return adds >= m

mid = (last+first)//2 ## 중간값
if(cutting(mid)): # 부합하면
    lastMid = mid
    while True: 
        mid = (last+first)//2 ## 중간값
        if(cutting(mid)): # 부합하면
            #더 올려도 됨
            first = mid
            lastMid = mid

        else:# 부합 안하면
            result = lastMid
            break#출력
#19 15 10 17
    

if cutting(mid) == False: # 부합안하면
    while True: 
        mid = (last+first)//2 ## 중간값
        if(cutting(mid)): # 부합하면
            #끝
            result = mid
            break
        else:# 부합 안하면
            last = mid
            #더 내림
#1 2 3 4 5
# ooo(o)x
# xxxxx(o)

print(result)