import pandas as pd
import numpy as np
def collatz(number):

    if number % 2 == 0:

        return number // 2

    elif number % 2 == 1:

        return 3 * number + 1


i=[]
c=[]
for j in range (10,2,-1):
    while j != 1:
        i.append(collatz(int(j)))

        n = collatz(int(j))
        c.append(len(i))
        max_value = max(c)

    print(c)