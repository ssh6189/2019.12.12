다형성 : 여러가지 형태를 가지는 특성

객체지향 - 다형성 개념
오버라이드(재정의)
오버로드(중복정의)

#너무 부담갖지는말자, 이 개념을 모른다고해서 못하는것은 아니다.

이미 다 만들어진것 가지고 잘 쓰면된다.

가져다 잘 쓰고, 남이 만든 코드에 대해 불편함이 없으면 된다.

이거 이해 못해서 못넘어간다. 이런 마음 안가져도 된다.



가시성

객체 정보접근을 숨긴다.
캡슐화, 정보은닉

객체의 정보를 볼 수 있는 레베를 조절하여 객체의 정보접근을 숨긴다.

파이썬의 가시성 사용 바법에 대한 예시 코드를 작성해야 하는 상황은 다음과 같다.
Product 객체를 Inventory 객체에 추가
Inventory에는 오직 Product 객체만 들어감
Inventory에 Product가 몇 개인지 확인이 필요
Inventory에 Product items는 직접 접근이 불가

예를들어
만약, 자동차가 있다.
이거 운전할 수만 있으면 되지, 이걸 일일이 뜯어서 개조를 하려다가 고장났다.

이것에 대해서는 책임 안져도 된다.

즉 in->f(x)->out

결과만 알면된다.

c에는 private 이 있고, 파이썬에는 __가 있다.

__에 대해서는 변경할 수 없다.

class Inventory(object):
    def __init__(self):
        self.__items = []

        @property
        def items(self):
            return self.__items

class person{
    private int salary;
    private int grade;#외부에서 접근 불가
    그러나, 외부에서 접근해야할때가 있다.
    public int getsalary(){}:#권한이 있을때만 값을 리턴하고, 아니면, 접근불가

    #직접은 엑세스 못하고, 필요하면 메서드를 이용해 접근가능하다.
     볼수는 있으나, 값변경은 못한다.
    
