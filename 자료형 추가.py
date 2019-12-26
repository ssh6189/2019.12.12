자료형

데이터모델
자료형에 대한 관리규칙
파이썬은 객체 지향개념을 수용해서 모든것을 객체로 관리한다.

만들어지는 모든 값은 객체를 처리하기 위해 속성을 메소드를 제공한다.

dir 함수 : 클래스와 인스턴스 내부에서 사용할 수 있는 정보를 확인
id 함수 : 클래스와 인스턴스의 레퍼런스를 정수로 리턴
type 메타 클래스 : 클래스와 인스턴스가 누구에 의해 만들어 졌는지에 대한 정보를 확인

print(object)
print(object.__str__object)) # 무조건 최상위 object가 있고 모든 객체는 상속을 받는다.
print(id(object))
print(object.__class__)
print(type(object))
print(object.__name__)
