import math

a=[]
for i in range(1,10):
    c = 0
    for b in range(i):
        c+=b
    a.append(c)

for x in range (1,10):
 d = 1
 for j in range (1,round(a[x]/2)+1):
    if a[x]%j==0:
        d += 1
 if (d >= 4):
     print(a[x], d)
