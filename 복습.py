python 에서 데이터를 효율적으로 메모리 저장하고, 검색, 반환, 관리를 위해 제공되는 자료구조



Stack LIFO(FILO)구조로서, list.append(), list.pop()

Queue FIFO(LILO)구조로서, list.append(), list.pop(0)



set 자료구조는 데이터를 저장할때 중복체크 후 중복되지 않았을때 저장함
집합연산 기능을 제공한다.

union(), |, difference(), -, intersection(), &



collections 모듈에서 제공해주는 객체

deque는 스택과 큐구조를 함께사용가능
OrderedDict dict의 key 또는 value를 기준으로 정렬해서 저장하는 구조

dict는 key에 대해서 unique해야하며, 존재하지 않는 key로 값을 꺼내면 Error발생

이런 에러를 해결할 수 있는 방법중 하나

1.dict.get("key", defaultValue)
2.defaultDict

Counter : 시퀀스 자료형의 데이터 요소개수를 딕셔너리 형태로 반환해주는 자료구조

문자열을 구분자를 이용해서 구분(토크나이징) : split()
여러 문자열을 구분자를 이용해서 하나의 문자열로 결합: join()



리스트컴프리헨션 : 필터링, map처리, reduce처리
[표현식 for 아이템 in (시퀀스자료형 또는 dict 자료형) if 조건]

[표현식 if 조건 표현식, else 표현식 for 아이템 in (시퀀스 자료형 또는 dict 자료형)]
[표현식 for 아이템1 in (시퀀스 자료형 또는 dict 자료형) for 아이템2 in (시퀀스 자료형 또는 dict 자료형)]

for 아이템1:
    for 아이템2:

꼴이 된다.

[[표현식 for 아이템1 in (시퀀스 자료형 또는 dict 자료형) for 아이템2 in (시퀀스 자료형 또는 dict 자료형)]]

for 

[[....][....][....]]


2버전은 자동, 3버전은 제너레이터 객체 반환
map(함수, 자료구조데이터객체(시퀀스나 변수)

3버전은
list(map(함수, 자료구조데이터객체(시퀀스나 변수)))

자료구조데이터객체 요소하나하나에 연산을해서 결과를 반환

reduce 함수

from fuctools import reduce

reduce(함수, 자료구조객체)는 자료구조의 데이터에 함수를 적용하여 통합(즉, 요약집계)처리할 때 사용

enumerate() 리스트로부터 데이터와 인덱스를 함께 반환

zip()여러 시퀀스객체들로 부터, 동일한 인덱스에 저장된 데이터를 묶어서 반환



def 함수이름(*매개변수): #가변매개변수이므로, 함수 호출시 가변인수 전달
def 함수이름(**매개변수): #키워드 가변 매개변수이므로 함수 호출시 이름=값 형태의 가변인수 전달

def 함수이름(매개변수):
    local1, local2, local3.... = *매개변수

    [[],[],[]] = **매개변수
    [(),(),()] = **매개변수 #unpacking

