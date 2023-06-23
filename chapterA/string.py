print("string\"\" ") # 백슬래시로 이스퀘이프 

print("hello"+" wolrd")
print("hello"*7)

print('hello'[2:3])
# 파이썬에선 문자열로 리스트와같이 내부적 처리

## 튜플 : 상수, 소괄호 사용
print((13,2,2))


## 딕셔너리 
#{}로 하면 안된다 {}는 집합이다. 
data = dict()
data['재관'] = '김'
data['재콴'] = '킴'
data['jaegwan'] = 'kim'

print(data)

if '재관' in data:
    print('in')
elif 'wor' in data:
    print('wor')

keyss = data.keys()
values = data.values()

print(keyss,values)


## 집합
# 순서가 없고 비중복적 , set([]) 혹은 {} 로

#집합의 연산
print({1,2,3}&{3,4,5})
print({1,2,3}|{3,4,5})
print({1,2,3}-{3,4,5})
setEx = {1,2}
setEx.add(10) #단일 추가
setEx.update([11,12])
setEx.remove(11)

print(setEx)
