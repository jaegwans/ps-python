#게임 개발

x,y = map(int, input().split()) # 맵 생성
ux, uy, ud = map(int,input().split()) # 좌표와 방향 0 북 1 2 3
mapArr = []
for _ in range(y):
    dmapArrItem = list(map(int,input().split()))
    mapArr.append(dmapArrItem)
    
# 규칙
# 1. 좌측에 안가본 칸 존재하면 좌측으로 회1전 후 한칸 전진
# 2. 안가본 칸 없으면 회전만 하고 다시 1단계
# 3. 사방 모두 가본 칸이면 or 바다 이면 바라보는 방향 유지한 체로 한칸 뒤로
# 3-1. 뒤가 바다면 움직임을 멈춤

# 북동남서
dx = [0,1,0,-1]
dy = [-1,0,1,0]
dd = [0,1,2,3]

log = [[ux,uy]]

stack = 0

while True:
    if stack == 5: ## 갈곳이 없으면 # 왜 5?  4면을 다 돌아보려면 5로 해야함
        stack = 0 # 스택 초기화
        if mapArr[uy+dy[ud-2]][ux+dx[ud-2]] == 0: # 뒤가 육지면
            ux += dx[ud-2] # 뒤로 이동
            uy += dy[ud-2]
            print(ux,uy,ud,'동작하나?')
            continue
        else: #뒤가 바다면
            print(ux,uy,ud)
            break # 멈춤
            
        
    
    if mapArr[uy+dy[ud-1]][ux+dx[ud-1]] == 0 and [uy+dy[ud-1],ux+dx[ud-1]] not in log: #좌측이 육지며 가보지 않은 곳이면
        ud = dd[ud-1] #회전 후 
        #전진
        ux += dx[ud]
        uy += dy[ud]
        log.append([ux,uy])
        print(ux,uy,ud)
    else: # 좌측이 육지며 가보지 않은것이 아닌 나머지
         ud = dd[ud-1] #회전 
         stack += 1
    
print(log)
print(len(log))
   
        
        
        
        
# 
