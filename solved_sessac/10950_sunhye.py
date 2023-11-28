t = int(input())

for i in range(t):
    A, B = map(int,input().split())
    print(A+B)
    
# 반복문이기 때문에 예외처리 안 해줘도 됨.
# map() 함수: 여러 개의 입력을 받을 경우
# 각 요소에 대해 특정한 함수를 적용시키고 싶을 때 사용
# 그냥 result = map(~) 해버리면 result에 저장되는 건
# map 메모리의 주소값. 따라서 리스트 형태로 저장 권유.
# list(map(int,input().split()))