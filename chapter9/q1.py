#미래도시
import sys
input = sys.stdin.readline
n,m = map(int,input().rstrip().split())
INF = int(1e9) # 주의
graph = [[INF]*(n+1) for i in range(n+1)]

for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b: # 주의
            graph[a][b] = 0

for i in range(1,m+1):
    x,y = map(int,input().rstrip().split())
    graph[x][y] = 1
    graph[y][x] = 1

x,k = map(int,input().rstrip().split()) # x:판매지 4 , k:소개팅장소 5

#FW f(n) = min(f(n),f(kn))
for a in range(1,n+1):
    for b in range(1,n+1):
        for c in range(1,n+1):
            graph[a][b] = min(graph[a][b],graph[a][c]+graph[c][b])# 주의
        
if ((graph[1][k]+graph[k][x])<INF): 
    print(graph[1][k]+graph[k][x]) 
    
else:
    print(-1)

#출력
for a in range(1,n+1): 
    for b in range(1,n+1):
        if graph[a][b]==INF:
            print('INF',end=" ")
        else:
            print(graph[a][b],end=" ")
        
    print() # 줄바꿈
    