from collections import deque
#미로 탈출
#괴물은 0 , 통로는 1
# 최소거리 -> BFS - 큐와 for문 
# 출구 n, m 
# 유저 0,0 부터 시작
# 출구 y-1,x-1
# append와 popleft

y,x = map(int,input().split())
graph = [] #그래프

for _ in range(y):
    graph.append(list(map(int,input())))

q = deque() # 큐
visited = [[False]*x for _ in range(y)] # 방문록
count = 0 # 카운트 

print(visited,graph)
q.append((0,0))
visited[0][0]= True

while True:
    
    if len(q)==0:
        break
    
    dy,dx = q.popleft()
    
    for ddy in [dy-1,dy,dy+1]:
        if -1<ddy<y:
            if  visited[ddy][dx]==False and graph[ddy][dx]==1:
                q.append((ddy,dx)) # 큐 추가 
                visited[ddy][dx] = True # 방명록
                graph[ddy][dx] = graph[dy][dx]+1 # 카운트 추가
                if ddy==y and dx==x:
                    break
      
            
    for ddx in [dx-1,dx,dx+1]:
      
        if -1<ddx<x:
            print(dy,ddx)
            if visited[dy][ddx]==False and graph[dy][ddx]==1:
                q.append((dy,ddx))
                visited[dy][ddx] = True
                graph[dy][ddx] = graph[dy][dx]+1
                if dy==y and ddx==x:
                    break

for i in range(y):
    for j in range(x):
        if visited[i][j] == True:
            count+=1

print(graph[y-1][x-1])

## 개선 점 
#dy dx 상하좌우를 미리 정의하여 효율적으로 상하좌우 탐색 필요
#bfs를 따로 함수로 뺴어 고치기 쉽게 할 필요가 있음