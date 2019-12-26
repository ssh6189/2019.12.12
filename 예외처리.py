예외 : 예상하지 못했는데, 프로그램 실행을 멈추게 하는 이벤트
기상청에서 비가 안온다고 했음, 소나기가 잠깐 옮, 그래도 기다렸다 목적지로감
예측가능한 예외와 예측 불가능한 예외가 존재

예측 가능한 예외 : 발생 여부를 개발자가 사전에 인지할 수 있는 예외이다. 개발자는
예외를 예측하여 명시적으로 예외가 발생할때는 어떻게 대응하라고 할 수 있다. 대표적으로
사용자 입력란에 값이 잘못들어갔다면, if문을 사용하여 사용자에게 잘못 입력했다고 응답하는
방법으로 매우 쉽게 대응이 가능하다.

예측 불가능한 예외 : 대표적으로 매우 많은 파일을 처리할 때 문제가 발생할 수 있다.
예측 불가능한 예외가 발생했을경우, 인터프리터가 자동으로 이것이 예외라고 사용자에게 알려준다.
대부분은 이러한 예외가 발생하면서 프로그램이 종료되므로 적절한 조치가 필요하다.

에러 : 프로그램 실행 자체가 안됨
    교통 수단이 자동차밖에 없는데, 지금, 자동차가 고장난 상황

대부분 개발자원인
프로그램을 개발하면서, 예상하지 못한 상황이 발생하는것 : 예측가능한 예외와 예측 불가능한
예외로 나눌 수 있다.

아이디 생성 오류 입력

자동 저장 기능




예외 처리 구문
try - excpet문
try:
    예외 발생 가능 코드
except 예외 타입:
    예외 발생시 실행되는 코드

예를 들어 보자

for i in range(10):
    try:
        print(10/i)
    except ZeroDivisionError:
        print("Not divided by 0")

가벼운 오류정도는 이런식으로 처리가 가능하다.

try except 구문이 for문 안에 있기 때문에, 중단되지 않았는데,

만약, try구문 안에 for문을 넣으면, 만약 예외가 발생하면, for문을 빠져나가 다음으로
넘어간다.



많이 존재하는 에러종류
IndexError
NameError
ZerodivisionError
ValueError
FileNotFoundError

try-except-else문

예외가 발생하지 않으면 수행
finally는 예외 발생여부와 상관없이 실행되는 코드



raise문

raise문은 try-except문과 달리 필요할때 예외를 발생시키는 코드이다.

raise 예외 타입(예외정보)



raise예제

while True:
    value = input("변환할 저웃값을 입력하시오.")
    for digit in value:
        if digit not in "0123456789":
            raise ValueError("숫자를 입력하지 않았습니다.")
        print("정수값을 입력한 숫자", value)


assert문

assert문은 미리 알아야 할 예외정보가 조건에 만족하지 않을경우 예외를 발생시키는 구문이다.

assert문 예제

def get_binary_number(decimal_number):
    assert isinstance(decimal_number, int)
    return bin(decimal_number)
print(get_binary_numbeer(10))
print(get_binary_number("10"))


        
