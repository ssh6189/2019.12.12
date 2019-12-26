class Person(object):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def about_me(self):
        print("hello")



class Employee(Person):
    def __init__(self, name, age, gender, hire_date):
        super().__init__(name, age, gender)
        self.salary = salary
        self.hire_date = hire_date

def do_work(self):
    print("일을 열심히 한다.")

def about_me(self):
    super().about_me()
    print("제 급여는", self.salary, "원이고, 제 입사일은", self.hire_date, "입니다.")

person1 = Person("사람1", 30, "남")
person1.about_me()
person1.do_work()

emp = employee("일꾼1", "남", 300, '2019/01/01')
emp1.about_me()
emp1.do_work()

#깊게는 안들어간다.
