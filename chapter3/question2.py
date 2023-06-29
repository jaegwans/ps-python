m,n = list(map(int,input().split()))
a1 = list(map(int,input().split()))
a2 = list(map(int,input().split()))
a3 = list(map(int,input().split()))
arr = []

arr.append(min(a1))
arr.append(min(a2))
arr.append(min(a3))
# m 행 n 열
print(max(arr))