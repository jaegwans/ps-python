#두 배열의 원소 교체
n,k = map(int,input().split())
# n: 원소 길이, k: 스왑 횟수 
# 결과 스왑 이후 최대 a배열의 합산
a = [] #오름차
b = [] #내림차 

a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]: # 스왑 해야함
        a[i],b[i] = b[i],a[i]


print(sum(a)) #sum은 내장함수

# n이 최대 10만이다. 대부분의 문제에서 1억 이하로 연산되게 해야하므로 n^2 미만의 정렬 알고리즘을 사용할 것