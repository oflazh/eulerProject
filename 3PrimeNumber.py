a = 11


for i in range(round(a/2)+1, 0, -1):
     if (a % i== 0 ):
        for j in range(2, i):
            if (i % j) == 0:
                break
            else:
             print(j)


