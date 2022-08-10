a=0
for i in range(100,1000):
    for j in range(100,1000):
        a=i*j
        if(int(a/100000)==a%10):
             if(int(a/10000)%10==int((a%100)/10)):
                 if(int(a/1000)%100%10==int((a%1000)/100)):
                  if(a>=906609):
                      print(a)

