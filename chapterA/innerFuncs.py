from itertools import permutations,combinations,product
from heapq  import heappush,heappop
from bisect import bisect_left,bisect_right
from collections import Counter,deque
import math
## 내장함수
a=[3,2,6,4,5]
b=[]
print(sum(a))
print(min(a))
print(eval("3+5"))

print(sorted(a))
print(sorted(a,reverse=True))


## itertools

print(list(permutations(a,5))) # 순열 : 5개를 뽑아 순서에 상관 있는 경우의 수 즉 5!
print(list(combinations(a,5))) # 조합 : 5개를 뽑아 순서에 상관 없는 경우의 수 즉 5/5
list(product(a,repeat=5)) # 프로덕트: 5개를 뽑에 순서에 상관 있게 나열 하나 중복을 허용함 ex(A,A)



## heaps : 우선순위큐

#heaps화

heappush(b,10)
print(b)
heappop(b)
print(b)

##bisect 이진탐색

# 정렬된 리스트에서 데이터를 삽입할 가장 좌측 혹은 우측 인덱스를 반환
# bisect_left(list,x)


##collections

#deque
data = deque(a)
data.pop()
data.popleft()
data.append(1)
data.appendleft(1)

#Counter
c = Counter(a)
c[1] # 1이 몇번 있는지 보여줌

#math
print(math.factorial(5))
print(math.sqrt(5))
print(math.gcd(10,15))

