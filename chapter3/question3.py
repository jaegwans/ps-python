n,k = list(map(int,input().split()))
count = 0

# n 은 어떤 수 k는 나눌 수

while True:
  
    if(n==1):
        break
    count += 1
    if(n%k==0):
        n = n/k
    else:
        n -= 1

print(count)
    
# 나누어지지 않으면 뺴고
# 나누어지면 나눈다.
# 횟수를 카운팅

#ex 25 5- > 7

# n이 k의 배수가 되어 나누기를 최대한 활용 