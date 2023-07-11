 #왕실의 나이트
 
 # x y좌표
 # 경우의수 8개중 가능한 경우의 수 a1
# 0~7
nite = str(input()) # 입력
list_x = ['a','b','c','d','e','f','g','h']
# L R U D
twice_x= [-2,2,0,0]
twice_y= [0,0,2,-2]
once_x = [-1,1,0,0]
once_y = [0,0,1,-1]

#문제별 더 효율적인 방법으로 풀기

y = int(nite[-1])-1 #숫자
 
x = list_x.index(nite[0]) # 영문

count = 0

for i in range(2): # 좌우
    dx = x
    dx += twice_x[i]
    if dx != x: # 두칸 전진한 경우만 
        for j in range(2,4): #상하
            dy = y
            dy += once_y[j]
            if dy != y: # 한칸 전진한 경우만
                if -1<dx<8 and -1<dy<8:
                    count += 1
            
for i in range(2,4): # 상하
    dy = y
   
    dy += twice_y[i]
    if dy != y:
        for j in range(2): #좌우
            dx = x
            dx += once_x[j]
    
            if dx != x:
                if -1<dx<8 and -1<dy<8 :
                    count += 1
            
print(count)