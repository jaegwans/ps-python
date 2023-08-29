# 효율적인 화패구성
#다시 풀어볼것
n,m = list(map(int,input().split(' ')))

coin = []

for _ in range(n):
    coin.append(int(input()))
    
d = [10001]*m+1 # 횟수 별로 점화식 세우기  만들 금액을 기준으로 판단
# f(n) = f(n-1) + (부합하는 최소횟수 수들)
d[0] = 0
if 1 in coin: 
    d[1] = 1
else:
    d[1] = 10001

if 1 in coin: 
    d[2] = 2
if 2 in coin:
    d[2] = 1


for i in range(3,m+1):
    d[i]= d[i-1] + 
    
    
    





print(n,m)