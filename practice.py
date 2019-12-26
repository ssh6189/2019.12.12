x = (49, 80, 20, 100, 80)
y = (43, 60, 85, 30, 90)
z = (49, 82, 48, 50, 100)

a, b, c, d, e = zip(x, y, z)

print(a,b,c,d,e)

print([sum(x) for x in (a, b, c, c, e)])
