
def collatz(number):

    if number % 2 == 0:

        return number // 2

    elif number % 2 == 1:

        return 3 * number + 1


for j in range (1000000,0,-1):

    i = []
    a = j
    while j != 1:
        k=0
        i.append(collatz(int(j)))

        j=collatz(int(j))
        if len(i)>0:
            k=len(i)

    if(len(i)>457):
     print(len(i), a)


