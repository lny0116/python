a={[1]:'python'}
print(a) #TypeError: unhashable type: 'list'

'''
구글링 참고
= 딕셔너리의 key의 원소는 hash할 수 있는 변형이 불가능한 값이어야 한다.
리스트는 변형이 가능한 타입이기 때문에 에러가 발생한 것 [이라고 생각]
'''