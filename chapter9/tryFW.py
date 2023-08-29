INF = int(1e9)

n = int(input())
m = int(input()) 

graph = [[INF]*(n+1) for _ in range(n+1)] # 그래프 입력받기/ 행: 출발, 렬: 도착

#자기 자신에게 가는 비용 초기화
for a in range(1,n+1):
    for b in range(1,n+1):
        if a == b:
            graph[a][b] = 0
            

#각 간선에 대한 정보 입력받기
for _ in range(m):
    # a에서 b로 가는 비용은 c다 
    a,b,c = map(int,input().split())
    graph[a][b]= c
    
# dp 플로이드 워셜 삼중 반복문 사용
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])
            
# 출력
for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b]==INF:
            print('INF',end=" ")
        else:
            print(graph[a][b],end=" ")
        
    print() # 줄바꿈
