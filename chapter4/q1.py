#상하좌우
#5
#R R R U D D
n = int(input())
plans = input().split()
x,y = 1,1
print(n,plans)
orders = ['L','R','U','D']
# L R U D
xx = [-1 , 1 , 0, 0]
yy = [0 , 0, -1, 1]


for plan in plans:
    # 초기화
    dx = x
    dy = y
    print(y,x)
   
    for i in range(4):
       if(plan == orders[i]):
           dx += xx[i]
           dy += yy[i]
           
   # 임시값
    if(dx<1 or dy<1 or dx>n or dy>n):
        continue
    x = dx
    y = dy
   

print(y,x)