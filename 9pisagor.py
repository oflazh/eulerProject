for a in range (1001):
    for b in range (a,1001):
        c=1000-a-b
        if (a * a + b * b == c * c):
            print(a * b * c)
            break

