import random

lotto = set()
count = 0

while(count<6):
    lotto.add(random.randrange(1,45))
    if len(lotto)==6:
            break
    else:
        pass

print(lotto)

str(input())
