import os

qu = int(input("몇번 입력하시겠습니까?"))

os.system("cls")

a = 0
b = 0

for k in range(qu):

    a = 0
    b = 0
    check = 0

    st = str(input("문자열을 입력하시오."))

    for i in range(len(st)):
        if(st[i] == "("):
            a = a + 1

        elif(st[i] == ")"):
            b = b + 1
        else:
            pass

        if(a >= b):
            if(st.count("(") >= st.count(")")):
                check = 1
            else:
                check = 0
        else:
            check = 0
            break


    if check == 0:
        print("NO")
    else:
        print("YES")

str(input())


