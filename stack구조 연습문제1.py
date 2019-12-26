import os

money = []

i = 0
s = 0

c = int(input("총 몇회 입력하시겠습니까?"))

while(i<c):
    print("돈을 입력하시오. 잘못 입력하신것을 지우시려면, 0을 입력하시오.""\n""(최근에 입력한것이 지워집니다.)")
    m = int(input())
    os.system("cls")
    
    if(m!=0):
        money.append(m)
        i = i + 1
    elif(i>0):
        money.pop()
        i = i + 1
    else:
        print("잘못 입력된 값이 없습니다!")
        i = i + 1
        pass

for j in range(len(money)):
    s = s + money[j]
    
print("총금액은", s, "원입니다.")

str(input())
