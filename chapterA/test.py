# 파이썬 복습

a = [1,2,3,4,5,6,7,8,9]

print(a[1:5])

print([i*2-1 for i in range(20)]) # 리스트 컴프리헨션

print([[0]* 4 for _ in range(4)]) # 2차원 배열은 반드시 이 방식으로 해야한다 

#만약 [[0]*4]*4 하면 참조가 복사되어 문제를 야기한다.

removeSet={3}
a.append(3)
a.remove(3)

removed = [i for i in a if i not in removeSet]

print(a)
print(removed)

